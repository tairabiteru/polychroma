function remove_all_but_last() {
    var background_elements = document.getElementsByClassName("background");
    for (let i = 0; i < background_elements.length; i++) {
        if (!(i == (background_elements.length - 1))) {
            background_elements[i].remove();
        }
    }
}