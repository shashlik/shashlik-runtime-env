import xdg.BaseDirectory
SHASHLIK_DIR         = "%s/shashlik" % xdg.BaseDirectory.xdg_data_home

SHASHLIK_INSTALL_DIR = "/opt/shashlik"
SHASHLIK_LIB_DIR     = "%s/lib64" % SHASHLIK_INSTALL_DIR
SHASHLIK_IMAGE_DIR   = "%s/android" % SHASHLIK_INSTALL_DIR
SHASHLIK_DATA_DIR    = "%s/data" % SHASHLIK_INSTALL_DIR
SHASHLIK_BIN_DIR     = "%s/bin" % SHASHLIK_INSTALL_DIR

SHASHLIK_ADB         = "%s/adb" % SHASHLIK_BIN_DIR
SHASHLIK_EMULATOR    = "%s/emulator64-x86" % SHASHLIK_BIN_DIR
SHASHLIK_AAPT        = "%s/aapt" % SHASHLIK_BIN_DIR
SHASHLIK_RUN         = "%s/shashlik_run" % SHASHLIK_BIN_DIR
