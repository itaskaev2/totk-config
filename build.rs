//! Embeds the icon (totk-config.rc, totk-config.ico) into totk-config.exe on Windows. With the GNU toolchain this runs
//! windres from MinGW-w64, the same PATH entry the windows crates need for dlltool.
//!
//! Also hands the tests TOTK_RECOMP_DIR: the TotK PC recomp checkout whose runtime/cfg.c, totk.ini.example and
//! docs/settings.md settings.json was made from. Default `upstream/` next to Cargo.toml (gitignored); the build itself
//! does not need it, only `cargo test` and tools/gen_configurator_settings.py do.
use std::path::PathBuf;

fn main() {
    println!("cargo:rerun-if-env-changed=TOTK_RECOMP_DIR");
    let manifest = PathBuf::from(std::env::var("CARGO_MANIFEST_DIR").unwrap());
    let recomp = std::env::var_os("TOTK_RECOMP_DIR").map(PathBuf::from).unwrap_or_else(|| manifest.join("upstream"));
    let recomp = if recomp.is_absolute() { recomp } else { manifest.join(recomp) };
    println!("cargo:rustc-env=TOTK_RECOMP_DIR={}", recomp.display().to_string().replace('\\', "/"));

    if std::env::var("CARGO_CFG_TARGET_OS").as_deref() == Ok("windows") {
        println!("cargo:rerun-if-changed=totk-config.ico");
        embed_resource::compile("totk-config.rc", embed_resource::NONE).manifest_optional().unwrap();
    }
}
