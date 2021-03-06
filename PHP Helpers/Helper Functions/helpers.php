<?php


/**
 * This helper function takes a collection returned from a laravel query and generates an associative array
 * consisting of the specified key => value pairs, which you can feed into Laravel's form facade to create
 * a database-backed drop-down list
 * You can also optionally prepend or append keys to the array. This is particularly useful if you want
 * to include options that are not necessarily returned by the database query
 * Use Case:
 * $all_cities = \App\City::all();
 * $dropdown_cities = dropdown_generator($all_cities, ['id' => 'title'], ['0' => 'No City']);
 * This will give you the following output:
 * ['0' => 'No City', '1' => 'Ismailia', '2' => 'Cairo'];
 * Note: that the given object should implement the ArrayAccess interface, which Laravel's collection does.
 */
function dropdown_generator($arr_obj, array $key_val, array $prepend = [], array $append = []) {
    $new_arr = $prepend;
    foreach($arr_obj as $item) {
        foreach ($key_val as $key => $val) {
            $new_arr[$item[$key]] = $item[$val];

        }
    }
    foreach ($append as $append_key => $append_val) {
        $new_arr[$append_key] = $append_val;

    }
    return $new_arr;

}

/**
 *This function is used to grab navigation bar links stored in a database in a parent/child style
 * It uses recursion to dynamically search through the links tree i.e It grabs a links children, and children
 * of children and so on.
 */
function r_link($parent_links, $fn = "children", $ch_key="children") {

    $result = [];
    foreach ($parent_links as $parent)
    {
        $parent_arr = $parent->toArray();
        if (!count($parent->$fn()->get()))
        {
            return [$parent->id => $parent_arr];
        }
        else
        {
            $parent_arr[$ch_key] = r_link($parent->$fn()->get());
        }
        $result[$parent->id] = $parent_arr;
    }
    return $result;

}
