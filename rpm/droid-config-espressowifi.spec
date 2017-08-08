# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device espressowifi
%define vendor samsung

%define vendor_pretty Samsung
%define device_pretty Galaxy Tab 2 WiFi

%define dcd_path ./

# Adjust this for your device
%define pixel_ratio 0.8

# Community HW adaptations need this
%define community_adaptation 1


# We assume most devices will
%define have_modem 0

%include droid-configs-device/droid-configs.inc
