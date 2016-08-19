extern crate chrono;
use chrono::*;

pub fn after(start: DateTime<UTC>) -> DateTime<UTC> {
    return start + Duration::seconds(1_000_000_000)
}
