//! Search-query parsing: operators, site:, filetype:, safe phrase quoting.

use crate::{SecurityError, MAX_QUERY_LEN};

/// Structured view of a parsed query.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ParsedQuery {
    pub terms: Vec<String>,
    pub phrases: Vec<String>,
    pub excluded: Vec<String>,
    pub site: Option<String>,
    pub filetype: Option<String>,
}

/// Parse a guarded query string into structured parts.
pub fn parse(raw: &str) -> Result<ParsedQuery, SecurityError> {
    let cleaned = crate::sanitize::clean_field(raw)?;
    if cleaned.len() > MAX_QUERY_LEN {
        return Err(SecurityError::TooLong { limit: MAX_QUERY_LEN, actual: cleaned.len() });
    }
    let mut q = ParsedQuery {
        terms: vec![],
        phrases: vec![],
        excluded: vec![],
        site: None,
        filetype: None,
    };
    let mut chars = cleaned.chars().peekable();
    let mut buf = String::new();
    while let Some(c) = chars.next() {
        match c {
            '"' => {
                let mut phrase = String::new();
                while let Some(p) = chars.next() {
                    if p == '"' { break; }
                    phrase.push(p);
                }
                if !phrase.trim().is_empty() { q.phrases.push(phrase.trim().to_string()); }
            }
            _ => {
                buf.push(c);
                if c == ' ' {
                    flush(&mut buf, &mut q);
                }
            }
        }
    }
    flush(&mut buf, &mut q);
    if q.terms.is_empty() && q.phrases.is_empty() {
        return Err(SecurityError::EmptyInput);
    }
    Ok(q)
}

fn flush(buf: &mut String, q: &mut ParsedQuery) {
    let token = buf.trim().to_lowercase();
    buf.clear();
    if token.is_empty() { return; }
    if let Some(rest) = token.strip_prefix("-") {
        if !rest.is_empty() { q.excluded.push(rest.to_string()); }
    } else if let Some(host) = token.strip_prefix("site:") {
        q.site = Some(host.to_string());
    } else if let Some(ft) = token.strip_prefix("filetype:") {
        q.filetype = Some(ft.to_string());
    } else {
        q.terms.push(token);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn parses_operators() {
        let q = parse("rust lang -old site:example.com filetype:pdf \"exact phrase\"").unwrap();
        assert!(q.terms.contains(&"rust".to_string()));
        assert!(q.excluded.contains(&"old".to_string()));
        assert_eq!(q.site.as_deref(), Some("example.com"));
        assert_eq!(q.filetype.as_deref(), Some("pdf"));
        assert_eq!(q.phrases, vec!["exact phrase".to_string()]);
    }

    #[test]
    fn rejects_empty() {
        assert!(parse("   ").is_err());
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
