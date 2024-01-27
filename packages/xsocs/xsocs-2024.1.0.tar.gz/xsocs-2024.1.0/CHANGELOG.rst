Change Log
==========

v2024.1.0: 2024/01/26
---------------------

- Added support for SXDM command from both BLISS and SPEC-like syntax (MR: !156)
- Fixed silx v2 support (MR: !157)
- Fixed FitWidget display (MR: !157)
- Fixed GUI issue with Python>=3.10 (MR: !154)
- Updated documentation (MR: !153, !155, !157, !159)
- Updated continuous integration (MR: !158, !159)

v2022.9.1: 2022/09/20
---------------------

- Added support of ID01 bliss data (MR: !151)

v2022.9.0: 2022/09/16
----------------------

Python >= 3.7 and silx >= 1.0.0 are required.
X-Socs is now a pure Python package (i.e., it does not contain compiled code).

* Bug fix:

  - Fixed support of bliss position dtype (MR: !139)
  - Fixed issue with colormap dialog (MR: !150)
  - Improved default number of cores guess (MR: !149)

* Compatibility:

  - Removed support of Python < 3.7 (MR: !144, !146)
  - Removed compatibility with `silx` < 1.0 (MR: !141)
  - Fixed `numpy` 1.20.0rc1 compatibility (MR: !133)

* Miscellaneous:

  - Major rework of the build/installation set-up of the project (MR: !137, !138, !143, !145, !147, !148)
  - Removed C extension (MR: !140)
  - Updated documentation (MR: !132)
  - Fixed continuous integration (MR: !134, !135, !136, !142)

v2020.11.0: 2020/11/13
----------------------

* Compatibility:

  - Fixed `h5py` v3 compatibility (MR: !130) and deprecation warnings (MR: !123, !128)
  - Fixed `silx` v0.14 issue (MR: !130) and v0.13 deprecation warnings (MR: !126, !129)

* Miscellaneous:

  - Update test environment (MR !124)
  - Build wheels for Python3.8 and 3.9 (MR !125, !131)
  - Update setup.py and test scripts (MR !127)


v2020.1.0: 2020/01/23
---------------------

* Bug fix:

  - Fix intensity computation issue on macOS by avoiding to save to HDF5 from multiprocessing part (MR: !120)
  - Fix Qspace conversion with median filter issue on debian8 by disabling OpenMP (MR: !114)

* Compatibility:

  - Avoid `h5py` deprecation warnings (MR: !121)
  - Improve compatibility with `PySide2` (MR: !118)
  - Make download during tests compatible with `silx` v0.11.0 (MR: !116)
  - Update tests after changes in dependencies (MR: !119)

* Documentation:

  - Update installation documentation (MR: !117)
  - Add description of HDF5 input file format to the documentation (MR: !115)
  - Update changelog (MR: !122)


v2019.1: 2019/02/08
-------------------

* Command line:

  - Add command `xsocs concat` to merge multiple HDF5 master files into one (MR: !54)
  - Add option `--numcores` to set number of cores to use, e.g., `xsocs gui --numcores 2` (MR: !78)
  - Add option `--no-3d` to disable OpenGL: `xsocs gui --no-3d` (MR: !84)

* Merge:

  - Add image ROI support to only save part of input images (MR: !60)
  - Read calibration and energy from spec when available (MR: !65)
  - Allow to merge inconsistent commands (MR: !56)

* Intensity view:

  - Allow to sort scans by any positioner not just eta (MR: !58)
  - Add colorbar and option to change scatter symbols and size (MR: !64)
  - Add selection of normalization (MR: !53)
  - Shift editor: Allow to display any measurement rather than intensity (MR: !97, !106)

* QSpace conversion:

  - Add QSpace spherical coordinates system (MR: !89)
  - Add image mask (MR: !59, !66)
  - Add maxipix correction (MR: !69)
  - Add multiple energies scan support (MR: !94, !98)
  - Add optional normalization (MR: !53)
  - Provide a default number of bins for QSpace histogram (MR: !73, !104)
  - Allow to override energy and calibration (MR: !50)
  - Update helper API (MR: !90)
  - Change HDF5 file management (MR: !111, !112)
  - QSpace view: Add a stack view of the QSpace as an alternative to 3D view (MR: !72)
  - QSpace view: Add a plot with the data histogram (MR: !108)

* Fit:

  - Add background subtraction of constant and 'snip' background (MR: !85, !86, !92, !103)
  - Improve QSpace projection on axes: normalize after projection (MR: !101, !102)
  - Add tests for COM (MR: !107)

* Compatibility:

  - Fix Python3 compatibility issues (Merge requests (MR): !44, !46, !51)
  - Add support of PyQt5 and drop PyQt4 support (MR: !61)
  - Deprecates Python2 support
  - Add dependency to fabio for EDF file reading (MR: !71, !77)
  - Add Windows support (MR: !74)

* Miscellaneous:

  - GUI: Usability improvements (MR: !47, !48, !49, !55, !68, !83, !95)
  - Tests: Use gitlab-ci for continuous integration on Linux (MR: !76, !110)
  - HDF5: Use gzip compression and allow to configure it (MR: !105)
  - Minor bug fixes (MR: !45, !70, !80, !91, !96, !99)
  - Clean-up, code style and project structure (MR: !62, !63, !82, !87, !88, !93)
  - Update documentation (MR: !52, !79, !109, !113)
  - Update to newer versions of dependencies (MR: !81)


v2017.1: 2017/12/15
-------------------
