# [0.32.0](https://github.com/andreoliwa/nitpick/compare/v0.31.0...v0.32.0) (2022-03-27)

### Bug Fixes

- **deps:** update dependency pytest-socket to a commit hash ([#440](https://github.com/andreoliwa/nitpick/issues/440)) ([61ac278](https://github.com/andreoliwa/nitpick/commit/61ac278a408ab1611b1c560dc3020c1a5eabb65b))
- GitHub URL should preserve query args ([#453](https://github.com/andreoliwa/nitpick/issues/453)) ([a2b97b1](https://github.com/andreoliwa/nitpick/commit/a2b97b1f4fd7be9f01030f462a3ad1832853deed))
- use built-in preset as default style ([#450](https://github.com/andreoliwa/nitpick/issues/450)) ([68fa2ce](https://github.com/andreoliwa/nitpick/commit/68fa2cee702f8ec83615ce00fe58a06169ea4788))

### Features

- add --version cli switch (thanks to [@mjpieters](https://github.com/mjpieters)) ([#468](https://github.com/andreoliwa/nitpick/issues/468)) ([6a85f79](https://github.com/andreoliwa/nitpick/commit/6a85f79882609393aa57a0f1b4292dd36d929087))
- resolve relative URIs in nitpick.styles.include ([#470](https://github.com/andreoliwa/nitpick/issues/470)) ([ec934dc](https://github.com/andreoliwa/nitpick/commit/ec934dce512807ec74d43b371e102a497ccfc13d))
- set initial style url(s) with nitpick init ([#473](https://github.com/andreoliwa/nitpick/issues/473)) ([0100f2b](https://github.com/andreoliwa/nitpick/commit/0100f2bc3b34fc058137872f1d4dfaed7f7e84f3))
- switch to requests-cache for style caching ([#467](https://github.com/andreoliwa/nitpick/issues/467)) ([c586d7f](https://github.com/andreoliwa/nitpick/commit/c586d7f5d9146fdcd13c2af727644284cc67f443))

# [0.31.0](https://github.com/andreoliwa/nitpick/compare/v0.30.0...v0.31.0) (2022-01-15)

### Bug Fixes

- keys suggested in the order they are defined ([#442](https://github.com/andreoliwa/nitpick/issues/442)) ([09c30ab](https://github.com/andreoliwa/nitpick/commit/09c30aba1b3438c286f2a2fc143044ff62126b2d))
- pin attrs to >=20.1.0, change imports ([0696d08](https://github.com/andreoliwa/nitpick/commit/0696d0813f2dd8e4e2776f506d31d1aff4ecb413))

### Features

- drop support for Python 3.6 ([#439](https://github.com/andreoliwa/nitpick/issues/439)) ([a02e0ce](https://github.com/andreoliwa/nitpick/commit/a02e0ce16e3e8fdbcc1caf23c33194ecd39a5dd3))

# [0.30.0](https://github.com/andreoliwa/nitpick/compare/v0.29.0...v0.30.0) (2022-01-14)

### Bug Fixes

- style override on Windows ([#422](https://github.com/andreoliwa/nitpick/issues/422)) ([e7d2897](https://github.com/andreoliwa/nitpick/commit/e7d2897096df3ab868c97b68d915191b488e83bf))
- use current dir; don't climb dirs to find the project root ([#421](https://github.com/andreoliwa/nitpick/issues/421)) ([3c82e8c](https://github.com/andreoliwa/nitpick/commit/3c82e8c4d019a5b25e1c0d9db1792f72cf800305))

### Features

- default pre-commit hook now runs "nitpick fix" ([cb4c242](https://github.com/andreoliwa/nitpick/commit/cb4c242607c6810c629dc7f5604920c1b64a070e))
- **json:** autofix JSON files ([#429](https://github.com/andreoliwa/nitpick/issues/429)) ([4b58a03](https://github.com/andreoliwa/nitpick/commit/4b58a0380f88b01c99945817e7ff9b595ea362aa))
- nitpick init adds a [tool.nitpick] section ([36f4065](https://github.com/andreoliwa/nitpick/commit/36f4065483b1ec4308bc28b815c82aa0abac104c))
- **yaml:** autofix .pre-commit-config.yaml (note: style changed!) ([#434](https://github.com/andreoliwa/nitpick/issues/434)) ([352b53d](https://github.com/andreoliwa/nitpick/commit/352b53d574e49ca683666fd40de3462d1396e575))
- **yaml:** autofix GitHub Workflow files ([#437](https://github.com/andreoliwa/nitpick/issues/437)) ([6af77c4](https://github.com/andreoliwa/nitpick/commit/6af77c4293d8f964ccd249626d47c82440e6412f))
- **yaml:** autofix YAML files ([#431](https://github.com/andreoliwa/nitpick/issues/431)) ([d8cc4b1](https://github.com/andreoliwa/nitpick/commit/d8cc4b1e80366d475c08316c54dc35393b4430dd))

# [0.29.0](https://github.com/andreoliwa/nitpick/compare/v0.28.0...v0.29.0) (2021-11-08)

### Bug Fixes

- convert ?token=xx into HTTP Basic creds for github style urls ([9b882a2](https://github.com/andreoliwa/nitpick/commit/9b882a26806431ec3c571fc5b130370b07539385))

### Features

- add Python 3.10 ([#410](https://github.com/andreoliwa/nitpick/issues/410)) ([050d2b9](https://github.com/andreoliwa/nitpick/commit/050d2b9642ca07e25300d12a2530311f18938972))
- add support for private Github repos for style sources ([49dc12d](https://github.com/andreoliwa/nitpick/commit/49dc12d9c5da7e1e71cb1a49d20a951a54d5e033))
- make generic.is_url() accept dollar-quoted userinfo fragments ([ef99acd](https://github.com/andreoliwa/nitpick/commit/ef99acd80fe11f827ca3edc744d31816eb242fe6))

# [0.28.0](https://github.com/andreoliwa/nitpick/compare/v0.27.0...v0.28.0) (2021-10-27)

### Bug Fixes

- remove() has changed to detach() on the ConfigUpdater API ([93c6c52](https://github.com/andreoliwa/nitpick/commit/93c6c52fdeff6dc35cbf66231a7f75fd8b6e99e8))

### Features

- read style from Python package (thanks to [@isac322](https://github.com/isac322)) ([#407](https://github.com/andreoliwa/nitpick/issues/407)) ([0a3c95d](https://github.com/andreoliwa/nitpick/commit/0a3c95d10b42011aaf7f9bfd5322e39cd71cd4af))

# [0.27.0](https://github.com/andreoliwa/nitpick/compare/v0.26.0...v0.27.0) (2021-07-20)

### Bug Fixes

- **cli:** print "no violations" message ([2fedd0a](https://github.com/andreoliwa/nitpick/commit/2fedd0a8b252972e06301cb1491054917af556d9))
- **cli:** replace the "run" command by "fix" and "check" ([#359](https://github.com/andreoliwa/nitpick/issues/359)) ([34d2499](https://github.com/andreoliwa/nitpick/commit/34d24993fed4de40c029d676a434761c19029860))
- don't fail when there is no config/root file ([#350](https://github.com/andreoliwa/nitpick/issues/350)) ([cca099a](https://github.com/andreoliwa/nitpick/commit/cca099a146f212d0e9ea2df26c12bfbc59706e80))
- include of remote style when there is only a local style ([#349](https://github.com/andreoliwa/nitpick/issues/349)) ([032855d](https://github.com/andreoliwa/nitpick/commit/032855dbd29f5ca9ddcc3a04ee93af13554d5afc))
- run pre-commit hooks only on passed files ([#356](https://github.com/andreoliwa/nitpick/issues/356)) ([3db024a](https://github.com/andreoliwa/nitpick/commit/3db024aa1f64972d9cc1d43c86a1eeb1632482aa))

### Features

- accept a regular GitHub URL as a style ([#361](https://github.com/andreoliwa/nitpick/issues/361)) ([8fc34cb](https://github.com/andreoliwa/nitpick/commit/8fc34cb32529d5f192a0433969563c70e32020a2))
- enforce settings on any TOML file ([#352](https://github.com/andreoliwa/nitpick/issues/352)) ([8fd6324](https://github.com/andreoliwa/nitpick/commit/8fd632459982d8df1456a33f24df5803234ba492))
- fetch GitHub URLs directly ([#341](https://github.com/andreoliwa/nitpick/issues/341)) ([d3e6811](https://github.com/andreoliwa/nitpick/commit/d3e6811c5c74307f0c618e5636f9043f0995f25b))
- install on macOS with Homebrew ([c679adf](https://github.com/andreoliwa/nitpick/commit/c679adf47e46fe89165b9a4d5158a38f30223550))
- pre-commit hook to apply changes ([#322](https://github.com/andreoliwa/nitpick/issues/322)) ([5e98e5f](https://github.com/andreoliwa/nitpick/commit/5e98e5fcda32d1fe40939bf3abd4e6e5da00e9ba))
- quick setup with `nitpick init` command ([#347](https://github.com/andreoliwa/nitpick/issues/347)) ([3156afe](https://github.com/andreoliwa/nitpick/commit/3156afe3ba9666a460b5ac84cfd82ab74a26605b))
- read configuration from `.nitpick.toml` or `pyproject.toml` ([#332](https://github.com/andreoliwa/nitpick/issues/332)) ([612ae41](https://github.com/andreoliwa/nitpick/commit/612ae41c6d0a71fd85ca0e37c136e3381978ec8c))
- root files for other programming languages ([#321](https://github.com/andreoliwa/nitpick/issues/321)) ([09a0e83](https://github.com/andreoliwa/nitpick/commit/09a0e838946a4b7cb615968fb524a9e18326cd7c))
- support custom protocols for styles ([#333](https://github.com/andreoliwa/nitpick/issues/333)) ([9baef63](https://github.com/andreoliwa/nitpick/commit/9baef630609f9c0b72acee5174494c652205a491))

# [0.26.0](https://github.com/andreoliwa/nitpick/compare/v0.25.0...v0.26.0) (2021-03-16)

### Features

- cache remote styles to avoid HTTP requests ([#312](https://github.com/andreoliwa/nitpick/issues/312)) ([08104d8](https://github.com/andreoliwa/nitpick/commit/08104d83d753a32d1438b79d7a100e10895ab79c))

# [0.25.0](https://github.com/andreoliwa/nitpick/compare/v0.24.1...v0.25.0) (2021-03-09)

### Features

- enforce configs for any INI file ([#304](https://github.com/andreoliwa/nitpick/issues/304)) ([80c840b](https://github.com/andreoliwa/nitpick/commit/80c840bc2d51cd25d82bcc4a59717c99f44c65ff))
- enforce settings on .editorconfig ([#305](https://github.com/andreoliwa/nitpick/issues/305)) ([e8b43d9](https://github.com/andreoliwa/nitpick/commit/e8b43d92edd97b8853acded9412cce526c54b953))
- enforce settings on .pylintrc ([#310](https://github.com/andreoliwa/nitpick/issues/310)) ([6aee663](https://github.com/andreoliwa/nitpick/commit/6aee6635030ff20d63706e1cc33e85f0da00c598))
- enforce settings on tox.ini ([#309](https://github.com/andreoliwa/nitpick/issues/309)) ([44d6cf4](https://github.com/andreoliwa/nitpick/commit/44d6cf4274ab007b0f499ee43062186fedfc45e8))

## [0.24.1](https://github.com/andreoliwa/nitpick/compare/v0.24.0...v0.24.1) (2021-02-28)

### Bug Fixes

- display parsing errors as violations ([#299](https://github.com/andreoliwa/nitpick/issues/299)) ([4e189eb](https://github.com/andreoliwa/nitpick/commit/4e189eb1113cca3a33f9821eb7aa3f45aace8b07))

# [0.24.0](https://github.com/andreoliwa/nitpick/compare/v0.23.1...v0.24.0) (2021-02-23)

### Bug Fixes

- check a YAML file with the text plugin ([#249](https://github.com/andreoliwa/nitpick/issues/249)) ([1821962](https://github.com/andreoliwa/nitpick/commit/1821962a2a1fce898d93a9e81a8663d9ae7c2aed))
- override a remote style with "./your-local-style.toml" ([#295](https://github.com/andreoliwa/nitpick/issues/295)) ([fe5f085](https://github.com/andreoliwa/nitpick/commit/fe5f085ef5200111ce4f4a2288a84091a96438e2))
- toml module now accepts keys beginning with dot (fix [#183](https://github.com/andreoliwa/nitpick/issues/183)) ([b086a24](https://github.com/andreoliwa/nitpick/commit/b086a24c5503c09e26ca429455bd4fea54cf01bb))
- validate sections in comma_separated_values (fix [#227](https://github.com/andreoliwa/nitpick/issues/227)) ([f1be98f](https://github.com/andreoliwa/nitpick/commit/f1be98f985ebcfc7e402f22271b428452a2f140b))

### Features

- fix pyproject.toml directly ([#287](https://github.com/andreoliwa/nitpick/issues/287)) ([4b79f81](https://github.com/andreoliwa/nitpick/commit/4b79f81f98430b749e7fa9ee5c192506d6ed5cf7))
- fix setup.cfg directly ([#288](https://github.com/andreoliwa/nitpick/issues/288)) ([f878630](https://github.com/andreoliwa/nitpick/commit/f87863066642cdab112d3145c488c9a780e7c98d))
- **cli:** add 'ls' command to list configured files ([cfc031b](https://github.com/andreoliwa/nitpick/commit/cfc031bdf30105dec9a8952bfb9657aec939b3b6))
- **cli:** add 'run' command to display violations ([a67bfa8](https://github.com/andreoliwa/nitpick/commit/a67bfa8bdaef2461853a237819cd35622c5935e9))
- **cli:** experimental CLI interface (alpha version) ([#255](https://github.com/andreoliwa/nitpick/issues/255)) ([c9ca5dc](https://github.com/andreoliwa/nitpick/commit/c9ca5dc3cc4586b459e2c58fb2e61d80aa3f1e5d))
- **cli:** filter only the desired files on ls/run commands ([#265](https://github.com/andreoliwa/nitpick/issues/265)) ([f5e4a9c](https://github.com/andreoliwa/nitpick/commit/f5e4a9c47583cd809941ca96ec2ffbdbf0c92c6f))
- drop support for Python 3.5 ([#251](https://github.com/andreoliwa/nitpick/issues/251)) ([9f84a60](https://github.com/andreoliwa/nitpick/commit/9f84a608a4ca02e8a96ec8eaaf55e5cb207b35e3)), closes [#250](https://github.com/andreoliwa/nitpick/issues/250)

## [0.23.1](https://github.com/andreoliwa/nitpick/compare/v0.23.0...v0.23.1) (2020-11-02)

### Bug Fixes

- upgrade toml to 0.10.2 (fixes [#200](https://github.com/andreoliwa/nitpick/issues/200)) ([3331e76](https://github.com/andreoliwa/nitpick/commit/3331e7621ccece6c2fb04aa0f50b802fd0a3367c))

# [0.23.0](https://github.com/andreoliwa/nitpick/compare/v0.22.2...v0.23.0) (2020-09-18)

### Bug Fixes

- get uiri/toml@9be6458 to fix conflict with black@20.8b1 ([fd2a44a](https://github.com/andreoliwa/nitpick/commit/fd2a44aedf253b0b73acec82b4c86b3fe3cc343f)), closes [#200](https://github.com/andreoliwa/nitpick/issues/200)

### Features

- check if a text file contains lines ([#182](https://github.com/andreoliwa/nitpick/issues/182)) ([3173bf7](https://github.com/andreoliwa/nitpick/commit/3173bf7380ef7b4e8221060cb575d606f6f4af2c))
- detect JSON files by extension, no need to declare them first ([6f54480](https://github.com/andreoliwa/nitpick/commit/6f544807867acc1b9234721000bf4c73838b5e72))
- use a plugin system (experimental) ([#180](https://github.com/andreoliwa/nitpick/issues/180)) ([6d2df4f](https://github.com/andreoliwa/nitpick/commit/6d2df4ffd156d9585c6a29bc7498a89e9b59ce16))

## [0.22.2](https://github.com/andreoliwa/nitpick/compare/v0.22.1...v0.22.2) (2020-05-15)

### Bug Fixes

- toml 0.10.1 is now raising ValueError: Circular reference ([ed1174f](https://github.com/andreoliwa/nitpick/commit/ed1174fcf27c82bb10ae0e45427ce6e284e62931)), closes [#159](https://github.com/andreoliwa/nitpick/issues/159)
- **json:** warn about different values ([4f9a891](https://github.com/andreoliwa/nitpick/commit/4f9a891f21d53a40b62f078b8dbd67076a144c5b)), closes [#155](https://github.com/andreoliwa/nitpick/issues/155)

## [0.22.1](https://github.com/andreoliwa/nitpick/compare/v0.22.0...v0.22.1) (2020-03-26)

### Bug Fixes

- broken build that didn't upload v0.22.0 to PyPI ([aaf2f06](https://github.com/andreoliwa/nitpick/commit/aaf2f06c7c563bd1388ebeb03a575b52461c6625))

# [0.22.0](https://github.com/andreoliwa/nitpick/compare/v0.21.4...v0.22.0) (2020-03-26)

### Bug Fixes

- consider any Python file (thanks [@tolusonaike](https://github.com/tolusonaike)) ([55c0965](https://github.com/andreoliwa/nitpick/commit/55c096529d40a95f53b13abf04a5b6aaabec0ed9)), closes [#138](https://github.com/andreoliwa/nitpick/issues/138)
- remove setup.py (thanks [@sobolevn](https://github.com/sobolevn) and [@bibz](https://github.com/bibz)) ([5d03744](https://github.com/andreoliwa/nitpick/commit/5d03744d1427997165dd4f11f8f68e0bef0a9083))

### Features

- add flag for offline mode ([#129](https://github.com/andreoliwa/nitpick/issues/129)) ([3650575](https://github.com/andreoliwa/nitpick/commit/36505753e245a065cffc683fc92b4391e72b3627))

## [0.21.4](https://github.com/andreoliwa/nitpick/compare/v0.21.3...v0.21.4) (2020-03-10)

### Bug Fixes

- display the current revision of the hook ([ee09be0](https://github.com/andreoliwa/nitpick/commit/ee09be0731654f72dbbf3d9dd316f476ae24c4cb))

## [0.21.3](https://github.com/andreoliwa/nitpick/compare/v0.21.2...v0.21.3) (2019-12-08)

### Bug Fixes

- concatenate URL manually instead of using Path ([5491b39](https://github.com/andreoliwa/nitpick/commit/5491b396e38aa8851bc7b01f4ecce583ef43655f)), closes [#115](https://github.com/andreoliwa/nitpick/issues/115)

## [0.21.2](https://github.com/andreoliwa/nitpick/compare/v0.21.1...v0.21.2) (2019-10-31)

### Bug Fixes

- infinite loop when climbing directories on Windows ([9915c74](https://github.com/andreoliwa/nitpick/commit/9915c74d52ab10d34b88733abb12958779e00ba8)), closes [#108](https://github.com/andreoliwa/nitpick/issues/108)

## [0.21.1](https://github.com/andreoliwa/nitpick/compare/v0.21.0...v0.21.1) (2019-09-23)

### Bug Fixes

- only check files if they have configured styles ([2cac863](https://github.com/andreoliwa/nitpick/commit/2cac863))

# [0.21.0](https://github.com/andreoliwa/nitpick/compare/v0.20.0...v0.21.0) (2019-08-26)

### Bug Fixes

- use green color to be compatible with click 6.7 ([54a6f4e](https://github.com/andreoliwa/nitpick/commit/54a6f4e)), closes [#81](https://github.com/andreoliwa/nitpick/issues/81)
- **json:** show original JSON key suggestion, without flattening ([d01cd05](https://github.com/andreoliwa/nitpick/commit/d01cd05))

### Features

- **style:** validate the [nitpick.files] section ([96c1c31](https://github.com/andreoliwa/nitpick/commit/96c1c31))
- show help with the documentation URL on validation errors ([83a8f89](https://github.com/andreoliwa/nitpick/commit/83a8f89))
- validate [nitpick.files.present] and [nitpick.files.absent] ([ab068b5](https://github.com/andreoliwa/nitpick/commit/ab068b5))
- validate configuration of JSON files ([e1192a4](https://github.com/andreoliwa/nitpick/commit/e1192a4))

# [0.20.0](https://github.com/andreoliwa/nitpick/compare/v0.19.0...v0.20.0) (2019-08-13)

### Bug Fixes

- report errors on line 0 instead of 1 ([31b13ea](https://github.com/andreoliwa/nitpick/commit/31b13ea)), closes [#73](https://github.com/andreoliwa/nitpick/issues/73)

### Features

- add config to check files that should be present ([408440f](https://github.com/andreoliwa/nitpick/commit/408440f)), closes [#74](https://github.com/andreoliwa/nitpick/issues/74)

# [0.19.0](https://github.com/andreoliwa/nitpick/compare/v0.18.0...v0.19.0) (2019-08-13)

### Bug Fixes

- emit warning when TOML is invalid in a style file (closes [#68](https://github.com/andreoliwa/nitpick/issues/68)) ([b48e0a4](https://github.com/andreoliwa/nitpick/commit/b48e0a4))
- files should not be deleted unless explicitly set in the style ([b5953ff](https://github.com/andreoliwa/nitpick/commit/b5953ff)), closes [#71](https://github.com/andreoliwa/nitpick/issues/71)
- improve the way to find the root dir of the project ([fa3460a](https://github.com/andreoliwa/nitpick/commit/fa3460a)), closes [#72](https://github.com/andreoliwa/nitpick/issues/72)

### Features

- validate the merged style file schema ([1e31d0a](https://github.com/andreoliwa/nitpick/commit/1e31d0a)), closes [#69](https://github.com/andreoliwa/nitpick/issues/69)

# [0.18.0](https://github.com/andreoliwa/nitpick/compare/v0.17.0...v0.18.0) (2019-08-09)

### Bug Fixes

- broken link on README (fixes [#70](https://github.com/andreoliwa/nitpick/issues/70), thanks [@sobolevn](https://github.com/sobolevn)) ([b35bbdb](https://github.com/andreoliwa/nitpick/commit/b35bbdb))

### Features

- **pyproject.toml:** validate [tool.nitpick] section ([765562a](https://github.com/andreoliwa/nitpick/commit/765562a))

# [0.17.0](https://github.com/andreoliwa/nitpick/compare/v0.16.1...v0.17.0) (2019-08-08)

### Bug Fixes

- **setup.cfg:** silently ignore invalid sections to avoid exceptions ([79cb441](https://github.com/andreoliwa/nitpick/commit/79cb441)), closes [#69](https://github.com/andreoliwa/nitpick/issues/69)

### Features

- highlight suggested changes with color ([f49f456](https://github.com/andreoliwa/nitpick/commit/f49f456))
- **json:** check if a JSON file contains the specified JSON data ([47fa133](https://github.com/andreoliwa/nitpick/commit/47fa133))
- **json:** check if a JSON file contains the specified keys ([0f8a53c](https://github.com/andreoliwa/nitpick/commit/0f8a53c))
- **json:** suggest content when file doesn't exist ([502eb3d](https://github.com/andreoliwa/nitpick/commit/502eb3d))
- **pre-commit:** add commitlint hook to the default recommended style ([61f467c](https://github.com/andreoliwa/nitpick/commit/61f467c))

## [0.16.1](https://github.com/andreoliwa/nitpick/compare/v0.16.0...v0.16.1) (2019-06-19)

### Bug Fixes

- don't try to remove the .cache root dir, it leads to errors sometimes ([856d8e7](https://github.com/andreoliwa/nitpick/commit/856d8e7))
- move flake8 plugins from nitpick to pre-commit ([7913e19](https://github.com/andreoliwa/nitpick/commit/7913e19))

# [0.16.0](https://github.com/andreoliwa/nitpick/compare/v0.15.0...v0.16.0) (2019-06-19)

### Features

- **pre-commit:** add nitpick hooks to use on .pre-commit-config.yaml ([92c13ae](https://github.com/andreoliwa/nitpick/commit/92c13ae))

# [0.15.0](https://github.com/andreoliwa/nitpick/compare/v0.14.0...v0.15.0) (2019-06-17)

### Features

- merge all styles into a single TOML file on the cache dir ([d803f64](https://github.com/andreoliwa/nitpick/commit/d803f64))
- **pre-commit:** compare missing and different keys on hooks ([#57](https://github.com/andreoliwa/nitpick/issues/57)) ([a8e2958](https://github.com/andreoliwa/nitpick/commit/a8e2958))

# [0.14.0](https://github.com/andreoliwa/nitpick/compare/v0.13.1...v0.14.0) (2019-06-07)

### Features

- rename project from "flake8-nitpick" to "nitpick" ([75be3b8](https://github.com/andreoliwa/nitpick/commit/75be3b8))

## [0.13.1](https://github.com/andreoliwa/nitpick/compare/v0.13.0...v0.13.1) (2019-06-07)

### Bug Fixes

- show warning about project being renamed to "nitpick" ([fda30fd](https://github.com/andreoliwa/nitpick/commit/fda30fd))

# [0.13.0](https://github.com/andreoliwa/nitpick/compare/v0.12.0...v0.13.0) (2019-06-06)

### Features

- run on Python 3.5 ([185e121](https://github.com/andreoliwa/nitpick/commit/185e121))

# [0.12.0](https://github.com/andreoliwa/nitpick/compare/v0.11.0...v0.12.0) (2019-06-03)

### Features

- get default style file from current version, not from master ([e0dccb8](https://github.com/andreoliwa/nitpick/commit/e0dccb8))

# [0.11.0](https://github.com/andreoliwa/nitpick/compare/v0.10.3...v0.11.0) (2019-03-31)

### Features

- allow pyproject.toml to be located in root dir's parents (thanks [@michael-k](https://github.com/michael-k)) ([#21](https://github.com/andreoliwa/nitpick/issues/21)) ([d3c4d74](https://github.com/andreoliwa/nitpick/commit/d3c4d74))

<a name="0.10.3"></a>

## [0.10.3](https://github.com/andreoliwa/nitpick/compare/v0.10.2...v0.10.3) (2019-03-13)

### Bug Fixes

- ignore FileNotFoundError when removing cache dir ([837bddf](https://github.com/andreoliwa/nitpick/commit/837bddf))

<a name="0.10.2"></a>

## [0.10.2](https://github.com/andreoliwa/nitpick/compare/v0.10.1...v0.10.2) (2019-03-13)

### Bug Fixes

- don't remove cache dir if it doesn't exist (FileNotFoundError) ([d5b6ec9](https://github.com/andreoliwa/nitpick/commit/d5b6ec9))

<a name="0.10.1"></a>

## [0.10.1](https://github.com/andreoliwa/nitpick/compare/v0.10.0...v0.10.1) (2019-03-11)

### Bug Fixes

- fetch private GitHub URLs with a token on the query string ([4cfc118](https://github.com/andreoliwa/nitpick/commit/4cfc118))

<a name="0.10.0"></a>

# [0.10.0](https://github.com/andreoliwa/nitpick/compare/v0.9.0...v0.10.0) (2019-03-11)

### Features

- assume style has a .toml extension when it's missing ([5a584ac](https://github.com/andreoliwa/nitpick/commit/5a584ac))
- read local style files from relative and other root dirs ([82d3675](https://github.com/andreoliwa/nitpick/commit/82d3675))
- read relative styles in subdirectories of a symlink dir ([55634e1](https://github.com/andreoliwa/nitpick/commit/55634e1))
- read styles from relative paths on URLs ([46d1b84](https://github.com/andreoliwa/nitpick/commit/46d1b84))

<a name="0.9.0"></a>

# [0.9.0](https://github.com/andreoliwa/nitpick/compare/v0.8.1...v0.9.0) (2019-03-06)

### Features

- improve error messages ([8a1ea4e](https://github.com/andreoliwa/nitpick/commit/8a1ea4e))
- minimum required version on style file ([4090cdc](https://github.com/andreoliwa/nitpick/commit/4090cdc))
- one style file can include another (also recursively) ([d963a8d](https://github.com/andreoliwa/nitpick/commit/d963a8d))

<a name="0.8.1"></a>

## [0.8.1](https://github.com/andreoliwa/nitpick/compare/v0.8.0...v0.8.1) (2019-03-04)

### Bug Fixes

- **setup.cfg:** comma separated values check failing on pre-commit ([27a37b6](https://github.com/andreoliwa/nitpick/commit/27a37b6))
- **setup.cfg:** comma separated values still failing on pre-commit, only on the first run ([36ea6f0](https://github.com/andreoliwa/nitpick/commit/36ea6f0))

<a name="0.8.0"></a>

# [0.8.0](https://github.com/andreoliwa/nitpick/compare/v0.7.1...v0.8.0) (2019-03-04)

### Bug Fixes

- keep showing other errors when pyproject.toml doesn't exist ([dc7f02f](https://github.com/andreoliwa/nitpick/commit/dc7f02f))
- move nitpick config to an exclusive section on the style file ([cd64361](https://github.com/andreoliwa/nitpick/commit/cd64361))
- use only yield to return values ([af7d8d2](https://github.com/andreoliwa/nitpick/commit/af7d8d2))
- use yaml.safe_load() ([b1df589](https://github.com/andreoliwa/nitpick/commit/b1df589))

### Features

- allow configuration of a missing message for each file ([fd053aa](https://github.com/andreoliwa/nitpick/commit/fd053aa))
- allow multiple style files ([22505ce](https://github.com/andreoliwa/nitpick/commit/22505ce))
- check root keys on pre-commit file (e.g.: fail_fast) ([9470aed](https://github.com/andreoliwa/nitpick/commit/9470aed))
- invalidate cache on every run ([e985a0a](https://github.com/andreoliwa/nitpick/commit/e985a0a))
- suggest initial contents for missing setup.cfg ([8d33b18](https://github.com/andreoliwa/nitpick/commit/8d33b18))
- suggest installing poetry ([5b6038c](https://github.com/andreoliwa/nitpick/commit/5b6038c))
- **pre-commit:** suggest pre-commit install ([76b980f](https://github.com/andreoliwa/nitpick/commit/76b980f))

### BREAKING CHANGES

- Comma separated values was moved to a different section in the TOML file:

Before:
["setup.cfg".nitpick]
comma_separated_values = ["food.eat"]

Now:
[nitpick.files."setup.cfg"]
comma_separated_values = ["food.eat"]

- The format of the absent files has changed in the style TOML file.

Before:
[[files.absent]]
file = "remove-this.txt"
message = "This file should be removed because of some reason"
[[files.absent]]
file = "another-useless-file-without-message.cfg"

Now:
[nitpick.files.absent]
"remove-this.txt" = "This file should be removed because of some reason"
"another-useless-file-without-message.cfg" = ""

<a name="0.7.1"></a>

## [0.7.1](https://github.com/andreoliwa/nitpick/compare/v0.7.0...v0.7.1) (2019-02-14)

### Bug Fixes

- Missing flake8 entry point on pyproject.toml ([a416007](https://github.com/andreoliwa/nitpick/commit/a416007))

<a name="0.7.0"></a>

# [0.7.0](https://github.com/andreoliwa/nitpick/compare/v0.6.0...v0.7.0) (2019-02-14)

### Features

- Suggest initial contents for missing .pre-commit-config.yaml ([16a6256](https://github.com/andreoliwa/nitpick/commit/16a6256))

<a name="0.6.0"></a>

# [0.6.0](https://github.com/andreoliwa/nitpick/compare/v0.5.0...v0.6.0) (2019-01-28)

### Features

- Configure comma separated values on the style file ([7ae6622](https://github.com/andreoliwa/nitpick/commit/7ae6622))
- Suggest poetry init when pyproject.toml does not exist ([366c2b6](https://github.com/andreoliwa/nitpick/commit/366c2b6))

### Bug Fixes

- DeprecationWarning: Using or importing the ABCs from 'collections' in ([80f7e24](https://github.com/andreoliwa/nitpick/commit/80f7e24))

<a name="0.5.0"></a>

# [0.5.0](https://github.com/andreoliwa/nitpick/compare/v0.4.0...v0.5.0) (2019-01-09)

### Features

- Add .venv to the absent files list ([153a7ca](https://github.com/andreoliwa/nitpick/commit/153a7ca))
- Add flake8-quotes to the default style ([60b3726](https://github.com/andreoliwa/nitpick/commit/60b3726))

<a name="0.4.0"></a>

# [0.4.0](https://github.com/andreoliwa/nitpick/compare/v0.3.0...v0.4.0) (2019-01-07)

### Features

- Check files that should not exist (like .isort.cfg) ([1901bb8](https://github.com/andreoliwa/nitpick/commit/1901bb8))
- Check pre-commit config file and the presence of hooks ([b1333db](https://github.com/andreoliwa/nitpick/commit/b1333db))
- Warn about replacing requirements.txt by pyproject.toml ([dacb091](https://github.com/andreoliwa/nitpick/commit/dacb091))

### Bug Fixes

- Don't break when pyproject.toml or setup.cfg don't exist ([6a546c1](https://github.com/andreoliwa/nitpick/commit/6a546c1))
- Only check rules if the file exists ([66e42d2](https://github.com/andreoliwa/nitpick/commit/66e42d2))

<a name="0.3.0"></a>

# [0.3.0](https://github.com/andreoliwa/nitpick/compare/v0.2.0...v0.3.0) (2019-01-03)

### Features

- Show different key/value pairs on pyproject.toml, case insensitive boolean values ([30e03eb](https://github.com/andreoliwa/nitpick/commit/30e03eb))

### Bug Fixes

- KeyError when section does not exist on setup.cfg ([e652604](https://github.com/andreoliwa/nitpick/commit/e652604))

<a name="0.2.0"></a>

# [0.2.0](https://github.com/andreoliwa/nitpick/compare/v0.1.1...v0.2.0) (2018-12-23)

### Features

- Check missing key/value pairs in pyproject.toml ([190aa6c](https://github.com/andreoliwa/nitpick/commit/190aa6c))
- Compare setup.cfg configuration ([2bf144a](https://github.com/andreoliwa/nitpick/commit/2bf144a))
- First warning, only on the main Python file ([0b30506](https://github.com/andreoliwa/nitpick/commit/0b30506))
- Read config from pyproject.toml, cache data, run only on one Python ([265daa5](https://github.com/andreoliwa/nitpick/commit/265daa5))
- Read style from TOML file/URL (or climb directory tree) ([84f19d6](https://github.com/andreoliwa/nitpick/commit/84f19d6))
- Respect the files section on nitpick.toml ([9e36a02](https://github.com/andreoliwa/nitpick/commit/9e36a02))
- Use nitpick's own default style file if none is provided ([4701b86](https://github.com/andreoliwa/nitpick/commit/4701b86))

<a name="0.1.1"></a>

## [0.1.1](https://github.com/andreoliwa/nitpick/compare/v0.1.0...v0.1.1) (2018-03-23)

README badges.

<a name="0.1.0"></a>

## 0.1.0 (2018-03-23)

First release.
