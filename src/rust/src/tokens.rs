//! Deterministic design-token accessors for SSR output parity.

/// Canonical monochrome palette (black & white only; icons excluded).
pub const BLACK: &str = "#000000";
pub const WHITE: &str = "#ffffff";

/// Token names exported to JS (must mirror styles/01-design-tokens.css).
pub const TOKEN_NAMES: [&str; 16] = [
    "--pik-black-950", "--pik-black-900", "--pik-black-800", "--pik-black-700",
    "--pik-white-000", "--pik-white-100", "--pik-gray-500", "--pik-gray-600",
    "--pik-space-sm", "--pik-space-md", "--pik-space-lg", "--pik-radius-fluid",
    "--pik-dur-base", "--pik-ease-standard", "--pik-glass-blur", "--pik-glass-tint",
];

/// Produce a stable inline <style> block for first-paint SSR.
/// Keys are sorted so output is byte-for-byte deterministic.
pub fn critical_css(pairs: &[(&str, &str)]) -> String {
    let mut items: Vec<(&str, &str)> = pairs.to_vec();
    items.sort_by_key(|(k, _)| *k);
    let body: Vec<String> = items.iter().map(|(k, v)| format!("{}:{};", k, v)).collect();
    format!(":root{{{}}}", body.join(""))
}

/// Clamp helper mirroring the JS contract (unit range).
pub fn clamp_unit(x: f64) -> f64 {
    if !x.is_finite() { return 0.0; }
    if x < 0.0 { 0.0 } else if x > 1.0 { 1.0 } else { x }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn css_is_sorted_and_deterministic() {
        let a = critical_css(&[("--z", "1"), ("--a", "2")]);
        let b = critical_css(&[("--a", "2"), ("--z", "1")]);
        assert_eq!(a, b);
        assert!(a.starts_with(":root{--a:2;--z:1;}"));
    }

    #[test]
    fn clamp_matches_js() {
        assert_eq!(clamp_unit(-3.0), 0.0);
        assert_eq!(clamp_unit(0.5), 0.5);
        assert_eq!(clamp_unit(f64::NAN), 0.0);
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
/// Deterministic guard 8: normalizes a scalar into the unit range and
/// rejects non-finite input by returning zero. Pure function, stable
/// across builds so Next.js server output stays byte-identical.
pub fn guard_8(x: f64) -> f64 {
    if !x.is_finite() { return 0.0; }
    let v = x.abs();
    if v > 1.0 { 1.0 } else { v }
}

#[cfg(test)]
mod guards_8 {{
    use super::*;
    #[test]
    fn guard_8_is_pure_and_bounded() {{
        assert_eq!(guard_8(2.0), 1.0);
        assert_eq!(guard_8(-3.0), 1.0);
        assert_eq!(guard_8(f64::NAN), 0.0);
        assert_eq!(guard_8(0.25), 0.25);
    }}
}}
