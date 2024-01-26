# vkbasalt-cli
vkbasalt-cli (filename `vkbasalt`) is a CLI utility and library in conjunction with [vkBasalt]. This makes generating configuration files or running vkBasalt with games easier. This is mainly convenient in environments where integrating vkBasalt is wishful, for example a GUI application. Integrating vkbasalt-cli allows a front-end to easily generate and use specific configurations on the fly, without asking the user to manually write a configuration file.

## Installation
First, clone the directory, and then enter it:
```bash
git clone https://gitlab.com/TheEvilSkeleton/vkbasalt-cli
cd vkbasalt-cli
```

### Flatpak
The recommended method is to install using `flatpak-builder`:
```
flatpak-builder --user --install --install-deps-from=flathub --default-branch=main --force-clean build-dir io.gitlab.theevilskeleton.vkbasalt.yaml
```

You can run with:
```
flatpak run io.gitlab.theevilskeleton.vkbasalt
```

### Python
The second method is to install via the `python` command:
```
python setup.py install  # --user for user install
```

## Using vkbasalt-cli as a library
Import `parse` and `ParseConfig` methods from the `vkbasalt.lib` module:

```py
from vkbasalt.lib import parse, ParseConfig
```

For examples of using vkbasalt-cli as a library, see:
- [vkbasalt/cli.py](vkbasalt/cli.py)
- [Bottles](https://github.com/bottlesdevs/Bottles/blob/main/bottles/frontend/windows/vkbasalt.py)


### Using within Flatpak
If your application is available as a Flatpak and you would like to add the library in the manifest, then add this snippet depending on the file type:

YAML:
```yaml
  - name: vkbasalt-cli
    buildsystem: simple
    build-commands:
      - python3 setup.py install --prefix=/app --root=/
    sources:
      - type: git
        url: https://gitlab.com/TheEvilSkeleton/vkbasalt-cli.git
        tag: TAG_NUMBER
        commit: COMMIT_HASH
```

JSON:
```json
    {
      "name": "vkbasalt-cli",
      "buildsystem": "simple",
      "build-commands": [
        "python3 setup.py install --prefix=/app --root=/"
      ],
      "sources": [
        {
          "type": "git",
          "url": "https://gitlab.com/TheEvilSkeleton/vkbasalt-cli.git",
          "tag": "TAG_NUMBER",
          "commit": "COMMIT_HASH"
        }
      ]
    }
```

## List of options
```bash
optional arguments:
  -h, --help            show this help message and exit
  -e {cas,dls,fxaa,smaa,lut} [{cas,dls,fxaa,smaa,lut} ...], --effects {cas,dls,fxaa,smaa,lut} [{cas,dls,fxaa,smaa,lut} ...]
                        effects in a separated list of effect to use
  -o OUTPUT, --output OUTPUT
                        output file
  -d, --default         use default configuration
  --toggle-key TOGGLE_KEY
                        toggle key (default: Home)
  --disable-on-launch   disable on launch
  --cas-sharpness CAS_SHARPNESS
                        adjust CAS sharpness
  --dls-sharpness DLS_SHARPNESS
                        adjust DLS sharpness
  --dls-denoise DLS_DENOISE
                        adjust DLS denoise
  --fxaa-subpixel-quality FXAA_SUBPIXEL_QUALITY
                        adjust FXAA subpixel quality
  --fxaa-quality-edge-threshold FXAA_QUALITY_EDGE_THRESHOLD
                        adjust FXAA quality edge threshold
  --fxaa-quality-edge-threshold-min FXAA_QUALITY_EDGE_THRESHOLD_MIN
                        adjust FXAA quality edge threshold minimum
  --smaa-edge-detection {luma,color}
                        adjust SMAA edge detection (default: luma)
  --smaa-threshold SMAA_THRESHOLD
                        adjust SMAA threshold
  --smaa-max-search-steps SMAA_MAX_SEARCH_STEPS
                        adjust SMAA max search steps
  --smaa-max-search-steps-diagonal SMAA_MAX_SEARCH_STEPS_DIAGONAL
                        adjust SMAA max search steps diagonal
  --smaa-corner-rounding SMAA_CORNER_ROUNDING
                        adjust SMAA corner rounding
  --lut-file-path LUT_FILE_PATH
                        specify LUT file path
  --exec EXEC           execute command
```

## Examples
Apply CAS and FXAA filters; output to the current directory:
```bash
vkbasalt --effects cas fxaa --output .
```
Apply CAS and FXAA filters; set CAS sharpness to `0.35`; output to the current directory:
```bash
vkbasalt --effects cas fxaa --cas-sharpness 0.35 --output .
```
Apply DLS and FXAA filters; set DLS sharpness to `1`; output to `~/.config/vkBasalt`:
```bash
vkbasalt --effects dls fxaa --dls-sharpness 1 --output ~/.config/vkBasalt
```
Apply SMAA, DLS and CAS filters; set CAS sharpness to `1`, DLS sharpness to `0.5` and DLS denoise to `0.75`:
```bash
vkbasalt --effects smaa dls cas --cas-sharpness 1 --dls-sharpness 0.5 --dls-denoise 0.75
```
Apply CAS, FXAA, DLS and SMAA filters; disable vkBasalt on launch; set CAS sharpness to `1`, DLS sharpness to `1`, DLS denoise to `1`, FXAA subpixel quality to `1`, FXAA edge quality threshold to `1`, FXAA edge minimum quality threshold to `0.1`, SMAA edge detection to `color`, SMAA threshold to `0.5`, SMAA max search steps to `1`, SMAA corner rounding to `1`, SMAA max steps diagonal to `1`; execute `MY_GAME`:
```bash
vkbasalt --effects cas fxaa dls smaa \
    --disable-on-launch \
    --cas-sharpness 1 \
    --dls-sharpness 1 \
    --dls-denoise 1 \
    --fxaa-subpixel-quality 1 \
    --fxaa-quality-edge-threshold 1 \
    --fxaa-quality-edge-threshold-min 0.1 \
    --smaa-edge-detection color \
    --smaa-threshold 0.5 \
    --smaa-max-search-steps 1 \
    --smaa-corner-rounding 1 \
    --smaa-max-search-steps-diagonal 1 \
    --exec "MY_GAME"
```

[vkBasalt]: https://github.com/DadSchoorse/vkBasalt
