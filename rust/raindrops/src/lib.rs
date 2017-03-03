pub fn raindrops(number: i32) -> String {

    let mut ret_str: String = String::new();

    if number % 3 == 0 {
        ret_str = format!("{}{}", ret_str, String::from("Pling"));
    }

    if number % 5 == 0 {
        ret_str = format!("{}{}", ret_str, String::from("Plang"));
    }

    if number % 7 == 0 {
        ret_str = format!("{}{}", ret_str, String::from("Plong"));
    }

    if (number % 3 != 0) & (number % 5 != 0) & (number % 7 != 0) {
        ret_str = number.to_string();
    }

    return ret_str;

}
