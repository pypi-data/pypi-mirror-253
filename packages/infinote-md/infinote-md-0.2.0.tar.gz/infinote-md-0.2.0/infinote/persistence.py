import json
from pathlib import Path

from colormath.color_conversions import convert_color
from colormath.color_objects import HSLColor, LCHabColor
from pynvim import Nvim

from infinote.buffer_handling import BufferHandler
from infinote.config import Config


def _name_to_hue(name: str):
    # choose the hue in a perceptually uniform way
    # choose a num between 60 and 310 degrees, to avoid non-persistent's red
    uniform = (name.__hash__() % 250) + 60  # note: this hash is changing
    random_lch_color = LCHabColor(100, 128, uniform)
    random_HSL_color = convert_color(random_lch_color, HSLColor)
    hue = int(random_HSL_color.hsl_h)
    return hue


def load_scene(buf_handler: BufferHandler, main_subdir: Path):
    filename_to_text = {}
    top_dir = main_subdir.parent
    top_dir.mkdir(parents=True, exist_ok=True)
    meta = {}

    if not main_subdir.exists():
        # save some initial hue for this dir
        hue = _name_to_hue(main_subdir.stem)
        meta[main_subdir.name] = dict(hue=hue)
        buf_handler.savedir_hues[main_subdir] = hue

    meta_path = top_dir / "meta.json"
    if not meta_path.exists():
        print(f"opening a new workspace in {top_dir}")
        # if there is no meta, top_dir should be empty
        assert not any(top_dir.iterdir()), f"top_dir not empty: {top_dir}"
        # create the main subdir
        main_subdir.mkdir(exist_ok=True)
        # create one text
        buf_handler.create_text(main_subdir, Config.initial_position)
        return

    # create the main subdir
    main_subdir.mkdir(exist_ok=True)
    meta.update(json.loads(meta_path.read_text()))
    subdirs = [d for d in top_dir.iterdir() if d.is_dir()]
    print(f"subdirs: {subdirs}")
    for subdir in subdirs:
        # load dir color
        assert subdir.name in meta, f"alien folder: {subdir}"
        buf_handler.savedir_hues[subdir] = meta[subdir.name]["hue"]

        # load files into buffers
        files = [f for f in subdir.iterdir() if f.suffix == ".md"]
        for full_filename in files:
            rel_filename = full_filename.relative_to(top_dir).as_posix()
            assert (
                full_filename.stem.isnumeric()
            ), f"names must be integers: {rel_filename}"
            assert rel_filename in meta, f"alien file: {rel_filename}"
            info = meta[rel_filename]

            # create text
            text = buf_handler.open_filename(
                info["plane_pos"], info["manual_scale"], full_filename.as_posix()
            )
            filename_to_text[rel_filename] = text

        # prepare the next file number
        
        max_filenum = max(int(f.stem) for f in files) if files else 0
        buf_handler.last_file_nums[subdir] = max_filenum

    # connect them
    for rel_filename, text in filename_to_text.items():
        info = meta[rel_filename]
        text.child_down = filename_to_text.get(info["child_down"])
        text.child_right = filename_to_text.get(info["child_right"])
        text.parent = filename_to_text.get(info["parent"])
    print(f"loaded {len(filename_to_text)} texts")


def save_scene(buf_handler: BufferHandler, nvim: Nvim, main_subdir: Path):
    top_dir = main_subdir.parent
    # record text metadata
    meta = {}
    for text in buf_handler.get_texts():
        if text.filename is None:
            # this buffer was not created by this program, so don't save it
            continue
        savedir = Path(text.filename).parent
        rel_filename = Path(text.filename).relative_to(top_dir).as_posix()
        meta[rel_filename] = dict(
            plane_pos=tuple(text.plane_pos.toTuple()),
            manual_scale=text.manual_scale,
            child_down=Path(text.child_down.filename).relative_to(top_dir).as_posix()
            if text.child_down
            else None,
            child_right=Path(text.child_right.filename).relative_to(top_dir).as_posix()
            if text.child_right
            else None,
            parent=Path(text.parent.filename).relative_to(top_dir).as_posix()
            if text.parent
            else None,
        )

    # record other data
    for subdir, hue in buf_handler.savedir_hues.items():
        meta["hue"] = buf_handler.savedir_hues[subdir]
        meta[subdir.name] = dict(hue=hue)

    # save metadata json
    meta_path = top_dir / "meta.json"
    meta_path.write_text(json.dumps(meta, indent=4))

    #########################################
    # save each text
    for text in buf_handler.get_texts():
        text.save(nvim)
