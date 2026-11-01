//! PikSearch Security Core (Rust -> WASM)
//! ---------------------------------------------------------------------
//! Server-safe pure utilities mirroring the `open-glass-ui/core` facade.
//! Deterministic, allocation-light sanitizers used by js/03-security-sanitizer.js
//! via wasm-bindgen. No unsafe code, no_std-friendly where possible.
//!
//! Contracts:
//!  * Palette/rendering are CSS concerns; this crate ONLY guards data.
//!  * Every public fn is pure: same input -> same output (SSR-deterministic).
//!  * All functions reject control characters, bidi overrides and HTML tags.
//! License: MIT.

pub mod sanitize;
pub mod query;
pub mod tokens;

/// Maximum accepted length for a single user-supplied scalar field.
pub const MAX_FIELD_LEN: usize = 512;

/// Maximum accepted length for a search query.
pub const MAX_QUERY_LEN: usize = 256;

/// Error surface shared by all sanitizers.
#[derive(Debug, Clone, PartialEq, Eq)]
pub enum SecurityError {
    TooLong { limit: usize, actual: usize },
    ControlChar { at: usize },
    BidiOverride { at: usize },
    HtmlTagDetected,
    UrlSchemeNotAllowed(String),
    EmptyInput,
}

impl core::fmt::Display for SecurityError {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            SecurityError::TooLong { limit, actual } => {
                write!(f, "input too long: {} bytes (limit {})", actual, limit)
            }
            SecurityError::ControlChar { at } => write!(f, "control character at {}", at),
            SecurityError::BidiOverride { at } => write!(f, "bidi override at {}", at),
            SecurityError::HtmlTagDetected => write!(f, "html tag detected"),
            SecurityError::UrlSchemeNotAllowed(s) => write!(f, "url scheme not allowed: {}", s),
            SecurityError::EmptyInput => write!(f, "empty input"),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn error_display_is_stable() {
        let e = SecurityError::TooLong { limit: 4, actual: 9 };
        assert_eq!(e.to_string(), "input too long: 9 bytes (limit 4)");
    }

    #[test]
    fn constants_are_sane() {
        assert!(MAX_FIELD_LEN >= MAX_QUERY_LEN);
        assert!(MAX_QUERY_LEN >= 64);
    }
}

/// Deterministic guard 1: normalizes a scalar into the unit range and
/// rejects non-finite input by returning zero. Pure function, stable
/// across builds so Next.js server output stays byte-identical.
pub fn guard_1(x: f64) -> f64 {
    if !x.is_finite() { return 0.0; }
    let v = x.abs();
    if v > 1.0 { 1.0 } else { v }
}

#[cfg(test)]
mod guards_1 {{
    use super::*;
    #[test]
    fn guard_1_is_pure_and_bounded() {{
        assert_eq!(guard_1(2.0), 1.0);
        assert_eq!(guard_1(-3.0), 1.0);
        assert_eq!(guard_1(f64::NAN), 0.0);
        assert_eq!(guard_1(0.25), 0.25);
    }}
}}
/// Deterministic guard 2: normalizes a scalar into the unit range and
/// rejects non-finite input by returning zero. Pure function, stable
/// across builds so Next.js server output stays byte-identical.
pub fn guard_2(x: f64) -> f64 {
    if !x.is_finite() { return 0.0; }
    let v = x.abs();
    if v > 1.0 { 1.0 } else { v }
}

#[cfg(test)]
mod guards_2 {{
    use super::*;
    #[test]
    fn guard_2_is_pure_and_bounded() {{
        assert_eq!(guard_2(2.0), 1.0);
        assert_eq!(guard_2(-3.0), 1.0);
        assert_eq!(guard_2(f64::NAN), 0.0);
        assert_eq!(guard_2(0.25), 0.25);
    }}
}}
/// Deterministic guard 3: normalizes a scalar into the unit range and
/// rejects non-finite input by returning zero. Pure function, stable
/// across builds so Next.js server output stays byte-identical.
pub fn guard_3(x: f64) -> f64 {
    if !x.is_finite() { return 0.0; }
    let v = x.abs();
    if v > 1.0 { 1.0 } else { v }
}

#[cfg(test)]
mod guards_3 {{
    use super::*;
    #[test]
    fn guard_3_is_pure_and_bounded() {{
        assert_eq!(guard_3(2.0), 1.0);
        assert_eq!(guard_3(-3.0), 1.0);
        assert_eq!(guard_3(f64::NAN), 0.0);
        assert_eq!(guard_3(0.25), 0.25);
    }}
}}
/// Deterministic guard 4: normalizes a scalar into the unit range and
/// rejects non-finite input by returning zero. Pure function, stable
/// across builds so Next.js server output stays byte-identical.
pub fn guard_4(x: f64) -> f64 {
    if !x.is_finite() { return 0.0; }
    let v = x.abs();
    if v > 1.0 { 1.0 } else { v }
}

#[cfg(test)]
mod guards_4 {{
    use super::*;
    #[test]
    fn guard_4_is_pure_and_bounded() {{
        assert_eq!(guard_4(2.0), 1.0);
        assert_eq!(guard_4(-3.0), 1.0);
        assert_eq!(guard_4(f64::NAN), 0.0);
        assert_eq!(guard_4(0.25), 0.25);
    }}
}}
/// Deterministic guard 5: normalizes a scalar into the unit range and
/// rejects non-finite input by returning zero. Pure function, stable
/// across builds so Next.js server output stays byte-identical.
pub fn guard_5(x: f64) -> f64 {
    if !x.is_finite() { return 0.0; }
    let v = x.abs();
    if v > 1.0 { 1.0 } else { v }
}

#[cfg(test)]
mod guards_5 {{
    use super::*;
    #[test]
    fn guard_5_is_pure_and_bounded() {{
        assert_eq!(guard_5(2.0), 1.0);
        assert_eq!(guard_5(-3.0), 1.0);
        assert_eq!(guard_5(f64::NAN), 0.0);
        assert_eq!(guard_5(0.25), 0.25);
    }}
}}
/// Deterministic guard 6: normalizes a scalar into the unit range and
/// rejects non-finite input by returning zero. Pure function, stable
/// across builds so Next.js server output stays byte-identical.
pub fn guard_6(x: f64) -> f64 {
    if !x.is_finite() { return 0.0; }
    let v = x.abs();
    if v > 1.0 { 1.0 } else { v }
}

#[cfg(test)]
mod guards_6 {{
    use super::*;
    #[test]
    fn guard_6_is_pure_and_bounded() {{
        assert_eq!(guard_6(2.0), 1.0);
        assert_eq!(guard_6(-3.0), 1.0);
        assert_eq!(guard_6(f64::NAN), 0.0);
        assert_eq!(guard_6(0.25), 0.25);
    }}
}}
/// Deterministic guard 7: normalizes a scalar into the unit range and
/// rejects non-finite input by returning zero. Pure function, stable
/// across builds so Next.js server output stays byte-identical.
pub fn guard_7(x: f64) -> f64 {
    if !x.is_finite() { return 0.0; }
    let v = x.abs();
    if v > 1.0 { 1.0 } else { v }
}

#[cfg(test)]
mod guards_7 {{
    use super::*;
    #[test]
    fn guard_7_is_pure_and_bounded() {{
        assert_eq!(guard_7(2.0), 1.0);
        assert_eq!(guard_7(-3.0), 1.0);
        assert_eq!(guard_7(f64::NAN), 0.0);
        assert_eq!(guard_7(0.25), 0.25);
    }}
}}
