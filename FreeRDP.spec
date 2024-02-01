#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: fae1327
#
Name     : FreeRDP
Version  : 3.2.0
Release  : 41
URL      : https://github.com/FreeRDP/FreeRDP/archive/3.2.0/FreeRDP-3.2.0.tar.gz
Source0  : https://github.com/FreeRDP/FreeRDP/archive/3.2.0/FreeRDP-3.2.0.tar.gz
Summary  : Free implementation of the Remote Desktop Protocol (RDP)
Group    : Development/Tools
License  : Apache-2.0
Requires: FreeRDP-bin = %{version}-%{release}
Requires: FreeRDP-lib = %{version}-%{release}
Requires: FreeRDP-license = %{version}-%{release}
BuildRequires : FreeRDP-dev
BuildRequires : SDL2-dev
BuildRequires : SDL2_ttf-dev
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-cmake
BuildRequires : cJSON-dev
BuildRequires : cups-dev
BuildRequires : docbook-xml
BuildRequires : extra-cmake-modules pkgconfig(libpulse)
BuildRequires : git
BuildRequires : glib-dev
BuildRequires : glibc-dev
BuildRequires : gst-plugins-base
BuildRequires : gst-plugins-base-dev
BuildRequires : gstreamer-dev
BuildRequires : icu4c-dev
BuildRequires : libSM-dev
BuildRequires : libX11-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libXcursor-dev
BuildRequires : libXdamage-dev
BuildRequires : libXext-dev
BuildRequires : libXi-dev
BuildRequires : libXinerama-dev
BuildRequires : libXv-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : libusb-dev
BuildRequires : libxkbfile-dev
BuildRequires : libxshmfence-dev
BuildRequires : libxslt-dev
BuildRequires : openssl-dev
BuildRequires : opus-dev
BuildRequires : opusfile-dev
BuildRequires : pcsc-lite-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(fuse3)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-app-1.0)
BuildRequires : pkgconfig(gstreamer-base-1.0)
BuildRequires : pkgconfig(gstreamer-video-1.0)
BuildRequires : pkgconfig(libcjson)
BuildRequires : pkgconfig(libpkcs11-helper-1)
BuildRequires : pkgconfig(libswscale)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(mit-krb5)
BuildRequires : pkgconfig(opus)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-scanner)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xrandr)
BuildRequires : qtbase-dev mesa-dev
BuildRequires : systemd-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
FreeRDP is a open and free implementation of the Remote Desktop Protocol (RDP).
This package provides nightly master builds of all components.

%package bin
Summary: bin components for the FreeRDP package.
Group: Binaries
Requires: FreeRDP-license = %{version}-%{release}

%description bin
bin components for the FreeRDP package.


%package dev
Summary: dev components for the FreeRDP package.
Group: Development
Requires: FreeRDP-lib = %{version}-%{release}
Requires: FreeRDP-bin = %{version}-%{release}
Provides: FreeRDP-devel = %{version}-%{release}
Requires: FreeRDP = %{version}-%{release}

%description dev
dev components for the FreeRDP package.


%package lib
Summary: lib components for the FreeRDP package.
Group: Libraries
Requires: FreeRDP-license = %{version}-%{release}

%description lib
lib components for the FreeRDP package.


%package license
Summary: license components for the FreeRDP package.
Group: Default

%description license
license components for the FreeRDP package.


%prep
%setup -q -n FreeRDP-3.2.0
cd %{_builddir}/FreeRDP-3.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1706799948
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake .. -DWITH_ALSA=ON \
-DWITH_CHANNELS=ON \
-DWITH_CLIENT=ON \
-DWITH_CLIENT_CHANNELS=ON \
-DWITH_CUPS=ON \
-DWITH_FFMPEG=OFF \
-DWITH_GSTREAMER_0_10=OFF \
-DWITH_GSTREAMER_1_0=ON \
-DWITH_JPEG=ON \
-DWITH_MANPAGES=ON \
-DWITH_OPENSSL=ON \
-DWITH_PULSE=ON \
-DWITH_SERVER=ON \
-DWITH_SERVER_CHANNELS=ON \
-DWITH_SHADOW_X11=ON \
-DWITH_SOXR=OFF \
-DWITH_SSE2=ON \
-DWITH_WAYLAND=ON \
-DWITH_X11=ON \
-DWITH_X264=OFF \
-DWITH_XCURSOR=ON \
-DWITH_XEXT=ON \
-DWITH_XI=ON \
-DWITH_XINERAMA=ON \
-DWITH_XKBFILE=ON \
-DWITH_XRENDER=ON \
-DWITH_XTEST=OFF \
-DWITH_XV=ON \
-DWITH_ZLIB=ON \
-DWITH_WEBVIEW=OFF \
-DWITH_MANPAGES=OFF
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DWITH_ALSA=ON \
-DWITH_CHANNELS=ON \
-DWITH_CLIENT=ON \
-DWITH_CLIENT_CHANNELS=ON \
-DWITH_CUPS=ON \
-DWITH_FFMPEG=OFF \
-DWITH_GSTREAMER_0_10=OFF \
-DWITH_GSTREAMER_1_0=ON \
-DWITH_JPEG=ON \
-DWITH_MANPAGES=ON \
-DWITH_OPENSSL=ON \
-DWITH_PULSE=ON \
-DWITH_SERVER=ON \
-DWITH_SERVER_CHANNELS=ON \
-DWITH_SHADOW_X11=ON \
-DWITH_SOXR=OFF \
-DWITH_SSE2=ON \
-DWITH_WAYLAND=ON \
-DWITH_X11=ON \
-DWITH_X264=OFF \
-DWITH_XCURSOR=ON \
-DWITH_XEXT=ON \
-DWITH_XI=ON \
-DWITH_XINERAMA=ON \
-DWITH_XKBFILE=ON \
-DWITH_XRENDER=ON \
-DWITH_XTEST=OFF \
-DWITH_XV=ON \
-DWITH_ZLIB=ON \
-DWITH_WEBVIEW=OFF \
-DWITH_MANPAGES=OFF
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1706799948
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/FreeRDP
cp %{_builddir}/FreeRDP-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/FreeRDP/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/FreeRDP-%{version}/include/freerdp/license.h %{buildroot}/usr/share/package-licenses/FreeRDP/b46488a80ea11f003740c3d3ec7fd7a008a681ce || :
cp %{_builddir}/FreeRDP-%{version}/libfreerdp/core/license.c %{buildroot}/usr/share/package-licenses/FreeRDP/87288c4edac47ab8fb5092529e2b478c59aea415 || :
cp %{_builddir}/FreeRDP-%{version}/libfreerdp/core/license.h %{buildroot}/usr/share/package-licenses/FreeRDP/34ed52a1bb3c94c8426221503c214487f2644d00 || :
cp %{_builddir}/FreeRDP-%{version}/winpr/libwinpr/sysinfo/cpufeatures/NOTICE %{buildroot}/usr/share/package-licenses/FreeRDP/ec4468ecfe59c46406d4fc5aca1cee2a83c4d93e || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/freerdp-proxy
/V3/usr/bin/freerdp-shadow-cli
/V3/usr/bin/sdl-freerdp
/V3/usr/bin/sfreerdp
/V3/usr/bin/sfreerdp-server
/V3/usr/bin/winpr-hash
/V3/usr/bin/winpr-makecert
/V3/usr/bin/wlfreerdp
/V3/usr/bin/xfreerdp
/usr/bin/freerdp-proxy
/usr/bin/freerdp-shadow-cli
/usr/bin/sdl-freerdp
/usr/bin/sfreerdp
/usr/bin/sfreerdp-server
/usr/bin/winpr-hash
/usr/bin/winpr-makecert
/usr/bin/wlfreerdp
/usr/bin/xfreerdp

%files dev
%defattr(-,root,root,-)
/usr/include/freerdp3/freerdp/addin.h
/usr/include/freerdp3/freerdp/altsec.h
/usr/include/freerdp3/freerdp/api.h
/usr/include/freerdp3/freerdp/assistance.h
/usr/include/freerdp3/freerdp/autodetect.h
/usr/include/freerdp3/freerdp/build-config.h
/usr/include/freerdp3/freerdp/buildflags.h
/usr/include/freerdp3/freerdp/cache/persistent.h
/usr/include/freerdp3/freerdp/channels/ainput.h
/usr/include/freerdp3/freerdp/channels/audin.h
/usr/include/freerdp3/freerdp/channels/channels.h
/usr/include/freerdp3/freerdp/channels/cliprdr.h
/usr/include/freerdp3/freerdp/channels/disp.h
/usr/include/freerdp3/freerdp/channels/drdynvc.h
/usr/include/freerdp3/freerdp/channels/echo.h
/usr/include/freerdp3/freerdp/channels/encomsp.h
/usr/include/freerdp3/freerdp/channels/geometry.h
/usr/include/freerdp3/freerdp/channels/gfxredir.h
/usr/include/freerdp3/freerdp/channels/location.h
/usr/include/freerdp3/freerdp/channels/log.h
/usr/include/freerdp3/freerdp/channels/rail.h
/usr/include/freerdp3/freerdp/channels/rdp2tcp.h
/usr/include/freerdp3/freerdp/channels/rdpdr.h
/usr/include/freerdp3/freerdp/channels/rdpecam.h
/usr/include/freerdp3/freerdp/channels/rdpei.h
/usr/include/freerdp3/freerdp/channels/rdpemsc.h
/usr/include/freerdp3/freerdp/channels/rdpewa.h
/usr/include/freerdp3/freerdp/channels/rdpgfx.h
/usr/include/freerdp3/freerdp/channels/rdpsnd.h
/usr/include/freerdp3/freerdp/channels/remdesk.h
/usr/include/freerdp3/freerdp/channels/scard.h
/usr/include/freerdp3/freerdp/channels/telemetry.h
/usr/include/freerdp3/freerdp/channels/tsmf.h
/usr/include/freerdp3/freerdp/channels/urbdrc.h
/usr/include/freerdp3/freerdp/channels/video.h
/usr/include/freerdp3/freerdp/channels/wtsvc.h
/usr/include/freerdp3/freerdp/client.h
/usr/include/freerdp3/freerdp/client/ainput.h
/usr/include/freerdp3/freerdp/client/audin.h
/usr/include/freerdp3/freerdp/client/channels.h
/usr/include/freerdp3/freerdp/client/client_cliprdr_file.h
/usr/include/freerdp3/freerdp/client/cliprdr.h
/usr/include/freerdp3/freerdp/client/cmdline.h
/usr/include/freerdp3/freerdp/client/disp.h
/usr/include/freerdp3/freerdp/client/drdynvc.h
/usr/include/freerdp3/freerdp/client/encomsp.h
/usr/include/freerdp3/freerdp/client/file.h
/usr/include/freerdp3/freerdp/client/geometry.h
/usr/include/freerdp3/freerdp/client/printer.h
/usr/include/freerdp3/freerdp/client/rail.h
/usr/include/freerdp3/freerdp/client/rdpei.h
/usr/include/freerdp3/freerdp/client/rdpgfx.h
/usr/include/freerdp3/freerdp/client/rdpsnd.h
/usr/include/freerdp3/freerdp/client/remdesk.h
/usr/include/freerdp3/freerdp/client/sshagent.h
/usr/include/freerdp3/freerdp/client/tsmf.h
/usr/include/freerdp3/freerdp/client/utils/smartcard_cli.h
/usr/include/freerdp3/freerdp/client/video.h
/usr/include/freerdp3/freerdp/codec/audio.h
/usr/include/freerdp3/freerdp/codec/bitmap.h
/usr/include/freerdp3/freerdp/codec/bulk.h
/usr/include/freerdp3/freerdp/codec/clear.h
/usr/include/freerdp3/freerdp/codec/color.h
/usr/include/freerdp3/freerdp/codec/dsp.h
/usr/include/freerdp3/freerdp/codec/h264.h
/usr/include/freerdp3/freerdp/codec/interleaved.h
/usr/include/freerdp3/freerdp/codec/jpeg.h
/usr/include/freerdp3/freerdp/codec/nsc.h
/usr/include/freerdp3/freerdp/codec/planar.h
/usr/include/freerdp3/freerdp/codec/progressive.h
/usr/include/freerdp3/freerdp/codec/region.h
/usr/include/freerdp3/freerdp/codec/rfx.h
/usr/include/freerdp3/freerdp/codec/yuv.h
/usr/include/freerdp3/freerdp/codec/zgfx.h
/usr/include/freerdp3/freerdp/codecs.h
/usr/include/freerdp3/freerdp/config.h
/usr/include/freerdp3/freerdp/constants.h
/usr/include/freerdp3/freerdp/crypto/ber.h
/usr/include/freerdp3/freerdp/crypto/certificate.h
/usr/include/freerdp3/freerdp/crypto/certificate_data.h
/usr/include/freerdp3/freerdp/crypto/certificate_store.h
/usr/include/freerdp3/freerdp/crypto/crypto.h
/usr/include/freerdp3/freerdp/crypto/der.h
/usr/include/freerdp3/freerdp/crypto/er.h
/usr/include/freerdp3/freerdp/crypto/per.h
/usr/include/freerdp3/freerdp/crypto/privatekey.h
/usr/include/freerdp3/freerdp/display.h
/usr/include/freerdp3/freerdp/dvc.h
/usr/include/freerdp3/freerdp/emulate/scard/smartcard_emulate.h
/usr/include/freerdp3/freerdp/error.h
/usr/include/freerdp3/freerdp/event.h
/usr/include/freerdp3/freerdp/extension.h
/usr/include/freerdp3/freerdp/freerdp.h
/usr/include/freerdp3/freerdp/gdi/bitmap.h
/usr/include/freerdp3/freerdp/gdi/dc.h
/usr/include/freerdp3/freerdp/gdi/gdi.h
/usr/include/freerdp3/freerdp/gdi/gfx.h
/usr/include/freerdp3/freerdp/gdi/pen.h
/usr/include/freerdp3/freerdp/gdi/region.h
/usr/include/freerdp3/freerdp/gdi/shape.h
/usr/include/freerdp3/freerdp/gdi/video.h
/usr/include/freerdp3/freerdp/graphics.h
/usr/include/freerdp3/freerdp/heartbeat.h
/usr/include/freerdp3/freerdp/input.h
/usr/include/freerdp3/freerdp/license.h
/usr/include/freerdp3/freerdp/listener.h
/usr/include/freerdp3/freerdp/locale/keyboard.h
/usr/include/freerdp3/freerdp/locale/locale.h
/usr/include/freerdp3/freerdp/log.h
/usr/include/freerdp3/freerdp/message.h
/usr/include/freerdp3/freerdp/metrics.h
/usr/include/freerdp3/freerdp/peer.h
/usr/include/freerdp3/freerdp/pointer.h
/usr/include/freerdp3/freerdp/primary.h
/usr/include/freerdp3/freerdp/primitives.h
/usr/include/freerdp3/freerdp/rail.h
/usr/include/freerdp3/freerdp/redirection.h
/usr/include/freerdp3/freerdp/scancode.h
/usr/include/freerdp3/freerdp/secondary.h
/usr/include/freerdp3/freerdp/server/ainput.h
/usr/include/freerdp3/freerdp/server/audin.h
/usr/include/freerdp3/freerdp/server/channels.h
/usr/include/freerdp3/freerdp/server/cliprdr.h
/usr/include/freerdp3/freerdp/server/disp.h
/usr/include/freerdp3/freerdp/server/drdynvc.h
/usr/include/freerdp3/freerdp/server/echo.h
/usr/include/freerdp3/freerdp/server/encomsp.h
/usr/include/freerdp3/freerdp/server/gfxredir.h
/usr/include/freerdp3/freerdp/server/location.h
/usr/include/freerdp3/freerdp/server/proxy/proxy_config.h
/usr/include/freerdp3/freerdp/server/proxy/proxy_context.h
/usr/include/freerdp3/freerdp/server/proxy/proxy_log.h
/usr/include/freerdp3/freerdp/server/proxy/proxy_modules_api.h
/usr/include/freerdp3/freerdp/server/proxy/proxy_server.h
/usr/include/freerdp3/freerdp/server/proxy/proxy_types.h
/usr/include/freerdp3/freerdp/server/rail.h
/usr/include/freerdp3/freerdp/server/rdpdr.h
/usr/include/freerdp3/freerdp/server/rdpecam-enumerator.h
/usr/include/freerdp3/freerdp/server/rdpecam.h
/usr/include/freerdp3/freerdp/server/rdpei.h
/usr/include/freerdp3/freerdp/server/rdpemsc.h
/usr/include/freerdp3/freerdp/server/rdpgfx.h
/usr/include/freerdp3/freerdp/server/rdpsnd.h
/usr/include/freerdp3/freerdp/server/remdesk.h
/usr/include/freerdp3/freerdp/server/server-common.h
/usr/include/freerdp3/freerdp/server/shadow.h
/usr/include/freerdp3/freerdp/server/telemetry.h
/usr/include/freerdp3/freerdp/session.h
/usr/include/freerdp3/freerdp/settings.h
/usr/include/freerdp3/freerdp/settings_keys.h
/usr/include/freerdp3/freerdp/settings_types.h
/usr/include/freerdp3/freerdp/settings_types_private.h
/usr/include/freerdp3/freerdp/streamdump.h
/usr/include/freerdp3/freerdp/svc.h
/usr/include/freerdp3/freerdp/transport_io.h
/usr/include/freerdp3/freerdp/types.h
/usr/include/freerdp3/freerdp/update.h
/usr/include/freerdp3/freerdp/utils/aad.h
/usr/include/freerdp3/freerdp/utils/cliprdr_utils.h
/usr/include/freerdp3/freerdp/utils/drdynvc.h
/usr/include/freerdp3/freerdp/utils/encoded_types.h
/usr/include/freerdp3/freerdp/utils/gfx.h
/usr/include/freerdp3/freerdp/utils/http.h
/usr/include/freerdp3/freerdp/utils/passphrase.h
/usr/include/freerdp3/freerdp/utils/pcap.h
/usr/include/freerdp3/freerdp/utils/pod_arrays.h
/usr/include/freerdp3/freerdp/utils/profiler.h
/usr/include/freerdp3/freerdp/utils/proxy_utils.h
/usr/include/freerdp3/freerdp/utils/rdpdr_utils.h
/usr/include/freerdp3/freerdp/utils/ringbuffer.h
/usr/include/freerdp3/freerdp/utils/signal.h
/usr/include/freerdp3/freerdp/utils/smartcard_call.h
/usr/include/freerdp3/freerdp/utils/smartcard_operations.h
/usr/include/freerdp3/freerdp/utils/smartcard_pack.h
/usr/include/freerdp3/freerdp/utils/smartcardlogon.h
/usr/include/freerdp3/freerdp/utils/stopwatch.h
/usr/include/freerdp3/freerdp/utils/string.h
/usr/include/freerdp3/freerdp/version.h
/usr/include/freerdp3/freerdp/window.h
/usr/include/rdtk0/rdtk/api.h
/usr/include/rdtk0/rdtk/build-config.h
/usr/include/rdtk0/rdtk/buildflags.h
/usr/include/rdtk0/rdtk/config.h
/usr/include/rdtk0/rdtk/rdtk.h
/usr/include/rdtk0/rdtk/version.h
/usr/include/uwac0/uwac/build-config.h
/usr/include/uwac0/uwac/buildflags.h
/usr/include/uwac0/uwac/config.h
/usr/include/uwac0/uwac/uwac-tools.h
/usr/include/uwac0/uwac/uwac.h
/usr/include/uwac0/uwac/version.h
/usr/include/winpr3/winpr/asn1.h
/usr/include/winpr3/winpr/assert.h
/usr/include/winpr3/winpr/bcrypt.h
/usr/include/winpr3/winpr/bitstream.h
/usr/include/winpr3/winpr/build-config.h
/usr/include/winpr3/winpr/buildflags.h
/usr/include/winpr3/winpr/clipboard.h
/usr/include/winpr3/winpr/cmdline.h
/usr/include/winpr3/winpr/collections.h
/usr/include/winpr3/winpr/comm.h
/usr/include/winpr3/winpr/config.h
/usr/include/winpr3/winpr/cred.h
/usr/include/winpr3/winpr/crt.h
/usr/include/winpr3/winpr/crypto.h
/usr/include/winpr3/winpr/custom-crypto.h
/usr/include/winpr3/winpr/debug.h
/usr/include/winpr3/winpr/dsparse.h
/usr/include/winpr3/winpr/endian.h
/usr/include/winpr3/winpr/environment.h
/usr/include/winpr3/winpr/error.h
/usr/include/winpr3/winpr/file.h
/usr/include/winpr3/winpr/handle.h
/usr/include/winpr3/winpr/image.h
/usr/include/winpr3/winpr/ini.h
/usr/include/winpr3/winpr/input.h
/usr/include/winpr3/winpr/interlocked.h
/usr/include/winpr3/winpr/intrin.h
/usr/include/winpr3/winpr/io.h
/usr/include/winpr3/winpr/library.h
/usr/include/winpr3/winpr/memory.h
/usr/include/winpr3/winpr/ncrypt.h
/usr/include/winpr3/winpr/nt.h
/usr/include/winpr3/winpr/ntlm.h
/usr/include/winpr3/winpr/pack.h
/usr/include/winpr3/winpr/path.h
/usr/include/winpr3/winpr/pipe.h
/usr/include/winpr3/winpr/platform.h
/usr/include/winpr3/winpr/pool.h
/usr/include/winpr3/winpr/print.h
/usr/include/winpr3/winpr/registry.h
/usr/include/winpr3/winpr/rpc.h
/usr/include/winpr3/winpr/sam.h
/usr/include/winpr3/winpr/schannel.h
/usr/include/winpr3/winpr/secapi.h
/usr/include/winpr3/winpr/security.h
/usr/include/winpr3/winpr/shell.h
/usr/include/winpr3/winpr/smartcard.h
/usr/include/winpr3/winpr/spec.h
/usr/include/winpr3/winpr/ssl.h
/usr/include/winpr3/winpr/sspi.h
/usr/include/winpr3/winpr/sspicli.h
/usr/include/winpr3/winpr/stream.h
/usr/include/winpr3/winpr/string.h
/usr/include/winpr3/winpr/strlst.h
/usr/include/winpr3/winpr/synch.h
/usr/include/winpr3/winpr/sysinfo.h
/usr/include/winpr3/winpr/tchar.h
/usr/include/winpr3/winpr/thread.h
/usr/include/winpr3/winpr/timezone.h
/usr/include/winpr3/winpr/tools/makecert.h
/usr/include/winpr3/winpr/user.h
/usr/include/winpr3/winpr/version.h
/usr/include/winpr3/winpr/wincrypt.h
/usr/include/winpr3/winpr/windows.h
/usr/include/winpr3/winpr/winpr.h
/usr/include/winpr3/winpr/winsock.h
/usr/include/winpr3/winpr/wlog.h
/usr/include/winpr3/winpr/wtsapi.h
/usr/include/winpr3/winpr/wtypes.h
/usr/lib64/cmake/FreeRDP-Client3/FreeRDP-ClientConfig.cmake
/usr/lib64/cmake/FreeRDP-Client3/FreeRDP-ClientConfigVersion.cmake
/usr/lib64/cmake/FreeRDP-Client3/FreeRDP-ClientTargets-relwithdebinfo.cmake
/usr/lib64/cmake/FreeRDP-Client3/FreeRDP-ClientTargets.cmake
/usr/lib64/cmake/FreeRDP-Proxy3/FreeRDP-ProxyConfig.cmake
/usr/lib64/cmake/FreeRDP-Proxy3/FreeRDP-ProxyConfigVersion.cmake
/usr/lib64/cmake/FreeRDP-Proxy3/FreeRDP-ProxyTargets-relwithdebinfo.cmake
/usr/lib64/cmake/FreeRDP-Proxy3/FreeRDP-ProxyTargets.cmake
/usr/lib64/cmake/FreeRDP-Server3/FreeRDP-ServerConfig.cmake
/usr/lib64/cmake/FreeRDP-Server3/FreeRDP-ServerConfigVersion.cmake
/usr/lib64/cmake/FreeRDP-Server3/FreeRDP-ServerTargets-relwithdebinfo.cmake
/usr/lib64/cmake/FreeRDP-Server3/FreeRDP-ServerTargets.cmake
/usr/lib64/cmake/FreeRDP-Shadow3/FreeRDP-ShadowConfig.cmake
/usr/lib64/cmake/FreeRDP-Shadow3/FreeRDP-ShadowConfigVersion.cmake
/usr/lib64/cmake/FreeRDP-Shadow3/FreeRDP-ShadowTargets-relwithdebinfo.cmake
/usr/lib64/cmake/FreeRDP-Shadow3/FreeRDP-ShadowTargets.cmake
/usr/lib64/cmake/FreeRDP3/FreeRDPConfig.cmake
/usr/lib64/cmake/FreeRDP3/FreeRDPConfigVersion.cmake
/usr/lib64/cmake/FreeRDP3/FreeRDPTargets-relwithdebinfo.cmake
/usr/lib64/cmake/FreeRDP3/FreeRDPTargets.cmake
/usr/lib64/cmake/WinPR-tools3/WinPR-toolsConfig.cmake
/usr/lib64/cmake/WinPR-tools3/WinPR-toolsConfigVersion.cmake
/usr/lib64/cmake/WinPR-tools3/WinPR-toolsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/WinPR-tools3/WinPR-toolsTargets.cmake
/usr/lib64/cmake/WinPR3/WinPRConfig.cmake
/usr/lib64/cmake/WinPR3/WinPRConfigVersion.cmake
/usr/lib64/cmake/WinPR3/WinPRTargets-relwithdebinfo.cmake
/usr/lib64/cmake/WinPR3/WinPRTargets.cmake
/usr/lib64/cmake/rdtk0/rdtk-relwithdebinfo.cmake
/usr/lib64/cmake/rdtk0/rdtk.cmake
/usr/lib64/cmake/rdtk0/rdtkConfig.cmake
/usr/lib64/cmake/rdtk0/rdtkConfigVersion.cmake
/usr/lib64/cmake/uwac0/uwac-relwithdebinfo.cmake
/usr/lib64/cmake/uwac0/uwac.cmake
/usr/lib64/cmake/uwac0/uwacConfig.cmake
/usr/lib64/cmake/uwac0/uwacConfigVersion.cmake
/usr/lib64/libfreerdp-client3.so
/usr/lib64/libfreerdp-server-proxy3.so
/usr/lib64/libfreerdp-server3.so
/usr/lib64/libfreerdp-shadow-subsystem3.so
/usr/lib64/libfreerdp-shadow3.so
/usr/lib64/libfreerdp3.so
/usr/lib64/librdtk0.so
/usr/lib64/libuwac0.so
/usr/lib64/libwinpr-tools3.so
/usr/lib64/libwinpr3.so
/usr/lib64/pkgconfig/freerdp-client3.pc
/usr/lib64/pkgconfig/freerdp-server-proxy3.pc
/usr/lib64/pkgconfig/freerdp-server3.pc
/usr/lib64/pkgconfig/freerdp-shadow3.pc
/usr/lib64/pkgconfig/freerdp3.pc
/usr/lib64/pkgconfig/rdtk0.pc
/usr/lib64/pkgconfig/uwac0.pc
/usr/lib64/pkgconfig/winpr-tools3.pc
/usr/lib64/pkgconfig/winpr3.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/freerdp3/proxy/proxy-bitmap-filter-plugin.so
/V3/usr/lib64/freerdp3/proxy/proxy-demo-plugin.so
/V3/usr/lib64/freerdp3/proxy/proxy-dyn-channel-dump-plugin.so
/V3/usr/lib64/libfreerdp-client3.so.3.2.0
/V3/usr/lib64/libfreerdp-server-proxy3.so.3.2.0
/V3/usr/lib64/libfreerdp-server3.so.3.2.0
/V3/usr/lib64/libfreerdp-shadow-subsystem3.so.3.2.0
/V3/usr/lib64/libfreerdp-shadow3.so.3.2.0
/V3/usr/lib64/libfreerdp3.so.3.2.0
/V3/usr/lib64/librdtk0.so.0.2.0
/V3/usr/lib64/libuwac0.so.0.2.0
/V3/usr/lib64/libwinpr-tools3.so.3.2.0
/V3/usr/lib64/libwinpr3.so.3.2.0
/usr/lib64/freerdp3/proxy/proxy-bitmap-filter-plugin.so
/usr/lib64/freerdp3/proxy/proxy-demo-plugin.so
/usr/lib64/freerdp3/proxy/proxy-dyn-channel-dump-plugin.so
/usr/lib64/libfreerdp-client3.so.3
/usr/lib64/libfreerdp-client3.so.3.2.0
/usr/lib64/libfreerdp-server-proxy3.so.3
/usr/lib64/libfreerdp-server-proxy3.so.3.2.0
/usr/lib64/libfreerdp-server3.so.3
/usr/lib64/libfreerdp-server3.so.3.2.0
/usr/lib64/libfreerdp-shadow-subsystem3.so.3
/usr/lib64/libfreerdp-shadow-subsystem3.so.3.2.0
/usr/lib64/libfreerdp-shadow3.so.3
/usr/lib64/libfreerdp-shadow3.so.3.2.0
/usr/lib64/libfreerdp3.so.3
/usr/lib64/libfreerdp3.so.3.2.0
/usr/lib64/librdtk0.so.0
/usr/lib64/librdtk0.so.0.2.0
/usr/lib64/libuwac0.so.0
/usr/lib64/libuwac0.so.0.2.0
/usr/lib64/libwinpr-tools3.so.3
/usr/lib64/libwinpr-tools3.so.3.2.0
/usr/lib64/libwinpr3.so.3
/usr/lib64/libwinpr3.so.3.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/FreeRDP/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/FreeRDP/34ed52a1bb3c94c8426221503c214487f2644d00
/usr/share/package-licenses/FreeRDP/87288c4edac47ab8fb5092529e2b478c59aea415
/usr/share/package-licenses/FreeRDP/b46488a80ea11f003740c3d3ec7fd7a008a681ce
/usr/share/package-licenses/FreeRDP/ec4468ecfe59c46406d4fc5aca1cee2a83c4d93e
