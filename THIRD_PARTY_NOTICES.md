# Third-party notices

What `totk-config.exe` and this repository contain that others wrote. The configurator's own code is MIT
([LICENSE](LICENSE)).

## The TotK PC recomp

https://github.com/valentderah/totk-pc-recomp, Copyright (c) 2026 Valiantsin Dzerakh, MIT. Taken from it:

| What | Where it comes from | Where it is here |
| --- | --- | --- |
| Setting names, defaults, values, sections, the in-game menu's tabs, groups, slider ranges and texts (English, Russian, Brazilian Portuguese, Simplified Chinese), key, button and action names and default bindings, setting descriptions | `runtime/cfg.c`, `runtime/ui/menu.cpp`, `runtime/ui/binds_page.cpp`, `runtime/ui/amiibo_page.cpp`, `runtime/ui_text.c`, `runtime/input_map.c`, `runtime/input_map.h`, `totk.ini.example`, `docs/settings.md`, read by `tools/gen_configurator_settings.py` at the version named in `Cargo.toml` | `settings.json` (generated, embedded in the exe) |
| The program icon (green ring), with a wrench added | `runtime/totk.ico` | `totk-config.ico` (`tools/make_configurator_icon.py`) |
| How `totk.ini` is read, migrated and written | `runtime/cfg.c` `cfg_load`, `cfg_save_to` (ported to Rust) | `src/ini.rs` |
| The in-game menu's colours | `runtime/ui/menu.cpp` `style_init` | `src/theme.rs` |

The recomp's licence:

```
MIT License

Copyright (c) 2026 Valiantsin Dzerakh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Font

| Component | Source | Licence | Where |
| --- | --- | --- | --- |
| Roboto Medium (unmodified) | https://fonts.google.com/specimen/Roboto, Copyright 2011 Google Inc.; the copy the recomp ships in `runtime/ui/fonts/` (from Dear ImGui's `misc/fonts/`) | Apache-2.0, text in [fonts/LICENSE-Roboto.txt](fonts/LICENSE-Roboto.txt) | `fonts/Roboto-Medium.ttf`, embedded in the exe by `src/theme.rs` |

CJK and symbol glyphs come from the system's own fonts at run time; none are shipped.

## Rust crates linked into the binaries

From `cargo tree -e normal --target <target>` at `Cargo.lock` (`python tools/third_party_crates.py` writes the tables
below). Most are under a choice of licences. `clipboard-win` and `error-code` (BSL-1.0) come with eframe's clipboard
support on Windows and cannot be left out; `unicode-ident` runs only at build time inside proc macros. On Windows HTTPS
goes through `ureq` with `native-tls` (Schannel and the Windows certificate store), so no TLS library or root
certificate list is linked in. On Linux it goes through `rustls` and `ring`, with the Mozilla root certificate list of
`webpki-roots` (CDLA-Permissive-2.0) built in; X11, Wayland and xkbcommon are loaded at run time from the system.

<!-- crate tables: tools/third_party_crates.py -->

### Windows: `totk-config.exe`

| Licence | Crates |
| --- | --- |
| (MIT OR Apache-2.0) AND Unicode-3.0 | unicode-ident v1.0.27 |
| 0BSD OR MIT OR Apache-2.0 | adler2 v2.0.1 |
| Apache-2.0 | glutin v0.32.3, glutin_egl_sys v0.7.1, glutin_wgl_sys v0.6.1, unicode-general-category v1.1.0, winit v0.30.13 |
| Apache-2.0 AND MIT | dpi v0.1.2 |
| Apache-2.0 OR GPL-2.0-only | self_cell v1.3.0 |
| Apache-2.0 OR MIT | base64ct v1.8.3, color v0.3.3, der v0.8.3, fearless_simd v0.4.1, kurbo v0.13.1, linebender_resource_handle v0.1.1, nohash-hasher v0.2.0, pem-rfc7468 v1.0.0, peniko v0.6.1, pin-project-lite v0.2.17, uuid v1.29.2, vello_common v0.1.0, vello_cpu v0.1.0, zeroize v1.9.1 |
| BSD-2-Clause OR Apache-2.0 OR MIT | zerocopy v0.8.63 |
| BSD-3-Clause OR Apache-2.0 | moxcms v0.8.1, pxfm v0.1.30 |
| BSL-1.0 | clipboard-win v5.4.3, error-code v3.4.0 |
| ISC | libloading v0.8.9 |
| MIT | bytes v1.12.1, generic-array v0.14.7, glutin-winit v0.5.0, harfrust v0.12.0, rfd v0.15.4, schannel v0.1.30, simd-adler32 v0.3.10, tracing v0.1.44, tracing-core v0.1.36, zmij v1.0.23 |
| MIT OR Apache-2.0 | accesskit v0.24.1, ahash v0.8.12, arboard v3.7.0, arrayvec v0.7.8, base64 v0.23.1, bitflags v2.13.2, block-buffer v0.10.4, cfg-if v1.0.5, cpufeatures v0.2.17, crc32fast v1.5.5, crypto-common v0.1.7, digest v0.10.7, document-features v0.2.12, ecolor v0.36.2, eframe v0.36.2, egui v0.36.2, egui-winit v0.36.2, egui_glow v0.36.2, either v1.19.0, emath v0.36.2, epaint v0.36.2, euclid v0.22.14, fdeflate v0.3.7, flate2 v1.1.11, font-types v0.12.7, hashbrown v0.17.1, http v1.5.0, httparse v1.10.1, image v0.25.10, itertools v0.15.0, itoa v1.0.19, litrs v1.0.1, lock_api v0.4.14, log v0.4.35, native-tls v0.2.18, num-traits v0.2.19, once_cell v1.21.4, parking_lot v0.12.5, parking_lot_core v0.9.12, percent-encoding v2.3.2, png v0.18.1, polycool v0.4.0, proc-macro2 v1.0.107, profiling v1.0.18, quote v1.0.47, read-fonts v0.41.0, rustls-pki-types v1.16.0, scopeguard v1.2.0, serde v1.0.229, serde_core v1.0.229, serde_derive v1.0.229, serde_json v1.0.154, sha2 v0.10.9, skrifa v0.44.0, smallvec v1.16.5, smol_str v0.2.2, static_assertions v1.1.0, syn v3.0.10, thiserror v2.0.21, thiserror-impl v2.0.21, typenum v1.20.1, unicode-segmentation v1.13.3, ureq v3.5.2, ureq-proto v0.7.1, utf8-zero v0.8.1, web-time v1.1.0, windows-link v0.2.1, windows-sys v0.52.0, windows-sys v0.59.0, windows-sys v0.61.2, windows-targets v0.52.6, windows_x86_64_msvc v0.52.6 |
| MIT OR Apache-2.0 OR Zlib | cursor-icon v1.2.0, glow v0.17.0, raw-window-handle v0.6.2 |
| MIT OR Zlib OR Apache-2.0 | miniz_oxide v0.8.9, miniz_oxide v0.9.1 |
| MIT/Apache-2.0 | guillotiere v0.7.0 |
| Unlicense OR MIT | byteorder-lite v0.1.0, memchr v2.8.3 |
| Zlib | foldhash v0.2.0 |
| Zlib OR Apache-2.0 OR MIT | bytemuck v1.25.2, bytemuck_derive v1.12.1 |

### Linux: `totk-config` in `totk-config-linux-x86_64.tar.gz`

| Licence | Crates |
| --- | --- |
| (MIT OR Apache-2.0) AND Unicode-3.0 | unicode-ident v1.0.27 |
| 0BSD OR MIT OR Apache-2.0 | adler2 v2.0.1 |
| Apache-2.0 | ab_glyph v0.2.32, ab_glyph_rasterizer v0.1.10, gethostname v1.1.0, glutin v0.32.3, glutin_egl_sys v0.7.1, glutin_glx_sys v0.6.1, owned_ttf_parser v0.25.1, unicode-general-category v1.1.0, winit v0.30.13 |
| Apache-2.0 AND ISC | ring v0.17.14 |
| Apache-2.0 AND MIT | dpi v0.1.2 |
| Apache-2.0 OR GPL-2.0-only | self_cell v1.3.0 |
| Apache-2.0 OR ISC OR MIT | rustls v0.23.46 |
| Apache-2.0 OR MIT | async-channel v2.5.0, async-executor v1.14.1, async-fs v2.2.0, async-io v2.6.0, async-lock v3.5.0, async-net v2.0.0, async-process v2.5.0, async-signal v0.2.14, async-task v4.7.1, atomic-waker v1.1.2, blocking v1.7.0, color v0.3.3, concurrent-queue v2.5.0, equivalent v1.0.3, event-listener v5.4.2, event-listener-strategy v0.5.4, fastrand v2.5.0, fearless_simd v0.4.1, futures-lite v2.6.1, idna_adapter v1.2.2, indexmap v2.14.2, kurbo v0.13.1, linebender_resource_handle v0.1.1, nohash-hasher v0.2.0, parking v2.2.1, peniko v0.6.1, pin-project-lite v0.2.17, polling v3.11.0, utf8_iter v1.1.0, utf_types v1.0.0, uuid v1.29.2, vello_common v0.1.0, vello_cpu v0.1.0, zeroize v1.9.1 |
| Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT | linux-raw-sys v0.12.1, linux-raw-sys v0.4.15, rustix v0.38.44, rustix v1.1.6 |
| Apache-2.0/MIT | pollster v0.4.0 |
| BSD-2-Clause | arrayref v0.3.9 |
| BSD-2-Clause OR Apache-2.0 OR MIT | zerocopy v0.8.63 |
| BSD-3-Clause | subtle v2.6.1, tiny-skia v0.11.4, tiny-skia-path v0.11.4 |
| BSD-3-Clause OR Apache-2.0 | moxcms v0.8.1, pxfm v0.1.30 |
| CDLA-Permissive-2.0 | webpki-roots v1.0.12 |
| ISC | libloading v0.8.9, rustls-webpki v0.103.17, untrusted v0.9.0 |
| MIT | ashpd v0.11.1, bytes v1.12.1, calloop v0.13.0, calloop v0.14.5, calloop-wayland-source v0.3.0, calloop-wayland-source v0.4.1, dlib v0.5.3, endi v1.1.1, generic-array v0.14.7, glutin-winit v0.5.0, harfrust v0.12.0, quick-xml v0.41.0, rfd v0.15.4, sctk-adwaita v0.10.1, simd-adler32 v0.3.10, slab v0.4.12, smithay-client-toolkit v0.19.2, smithay-client-toolkit v0.20.0, smithay-clipboard v0.7.3, strict-num v0.1.1, synstructure v0.14.0, tracing v0.1.44, tracing-attributes v0.1.31, tracing-core v0.1.36, urlencoding v2.1.3, wayland-backend v0.3.17, wayland-client v0.31.15, wayland-csd-frame v0.3.0, wayland-cursor v0.31.14, wayland-protocols v0.32.13, wayland-protocols-experimental v20250721.0.1, wayland-protocols-misc v0.3.12, wayland-protocols-plasma v0.3.12, wayland-protocols-wlr v0.3.12, wayland-scanner v0.31.11, wayland-sys v0.31.11, winnow v1.0.5, x11-dl v2.21.0, xcursor v0.3.11, xkbcommon-dl v0.4.2, zbus v5.19.0, zbus_macros v5.19.0, zbus_names v4.3.5, zcheapstr v1.2.0, zmij v1.0.23, zvariant v5.15.1, zvariant_derive v5.15.1, zvariant_utils v4.2.0 |
| MIT OR Apache-2.0 | accesskit v0.24.1, ahash v0.8.12, arboard v3.7.0, arrayvec v0.7.8, as-raw-xcb-connection v1.0.1, async-broadcast v0.7.2, async-recursion v1.2.0, async-trait v0.1.92, base64 v0.23.1, bitflags v2.13.2, block-buffer v0.10.4, cfg-if v1.0.5, cpufeatures v0.2.17, crc32fast v1.5.5, crossbeam-utils v0.8.23, crypto-common v0.1.7, digest v0.10.7, displaydoc v0.2.7, document-features v0.2.12, ecolor v0.36.2, eframe v0.36.2, egui v0.36.2, egui-winit v0.36.2, egui_glow v0.36.2, either v1.19.0, emath v0.36.2, enumflags2 v0.7.12, enumflags2_derive v0.7.12, epaint v0.36.2, errno v0.3.15, euclid v0.22.14, fdeflate v0.3.7, flate2 v1.1.11, font-types v0.12.7, form_urlencoded v1.2.2, futures-channel v0.3.34, futures-core v0.3.34, futures-io v0.3.34, futures-macro v0.3.34, futures-task v0.3.34, futures-util v0.3.34, getrandom v0.2.17, getrandom v0.3.4, hashbrown v0.17.1, hex v0.4.3, http v1.5.0, httparse v1.10.1, idna v1.1.0, image v0.25.10, itertools v0.15.0, itoa v1.0.19, libc v0.2.191, litrs v1.0.1, lock_api v0.4.14, log v0.4.35, memmap2 v0.9.12, num-traits v0.2.19, once_cell v1.21.4, ordered-stream v0.2.0, parking_lot v0.12.5, parking_lot_core v0.9.12, percent-encoding v2.3.2, piper v0.2.5, png v0.18.1, polycool v0.4.0, ppv-lite86 v0.2.21, proc-macro-crate v3.5.0, proc-macro2 v1.0.107, profiling v1.0.18, quote v1.0.47, rand v0.9.5, rand_chacha v0.9.0, rand_core v0.9.5, read-fonts v0.41.0, rustls-pki-types v1.16.0, scopeguard v1.2.0, serde v1.0.229, serde_core v1.0.229, serde_derive v1.0.229, serde_json v1.0.154, serde_repr v0.1.21, sha2 v0.10.9, signal-hook-registry v1.4.8, skrifa v0.44.0, smallvec v1.16.5, smol_str v0.2.2, stable_deref_trait v1.2.1, static_assertions v1.1.0, syn v2.0.119, syn v3.0.10, thiserror v1.0.69, thiserror v2.0.21, thiserror-impl v1.0.69, thiserror-impl v2.0.21, toml_datetime v1.1.3+spec-1.1.0, toml_edit v0.25.19+spec-1.1.0, toml_parser v1.1.5+spec-1.1.0, ttf-parser v0.25.1, typenum v1.20.1, unicode-segmentation v1.13.3, ureq v3.5.2, ureq-proto v0.7.1, url v2.5.8, utf8-zero v0.8.1, web-time v1.1.0, x11rb v0.13.2, x11rb-protocol v0.13.2 |
| MIT OR Apache-2.0 OR Zlib | cursor-icon v1.2.0, glow v0.17.0, raw-window-handle v0.6.2, xkeysym v0.2.1 |
| MIT OR Zlib OR Apache-2.0 | miniz_oxide v0.8.9, miniz_oxide v0.9.1 |
| MIT/Apache-2.0 | downcast-rs v1.2.1, guillotiere v0.7.0, scoped-tls v1.0.1 |
| Unicode-3.0 | icu_collections v2.4.0, icu_locale_core v2.4.0, icu_normalizer v2.4.0, icu_normalizer_data v2.4.0, icu_properties v2.4.0, icu_properties_data v2.4.0, icu_provider v2.4.0, litemap v0.8.3, potential_utf v0.1.6, tinystr v0.8.5, writeable v0.6.4, yoke v0.8.4, yoke-derive v0.8.4, zerofrom v0.1.8, zerofrom-derive v0.1.8, zerotrie v0.2.5, zerovec v0.11.9, zerovec-derive v0.11.7 |
| Unlicense OR MIT | byteorder-lite v0.1.0, memchr v2.8.3 |
| Zlib | foldhash v0.2.0 |
| Zlib OR Apache-2.0 OR MIT | bytemuck v1.25.2, bytemuck_derive v1.12.1 |
