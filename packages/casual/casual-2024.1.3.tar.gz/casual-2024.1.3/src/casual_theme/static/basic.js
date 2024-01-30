// Initialize the Side MetisMenu only if the element exists
if (document.getElementById('side-mm')) {
    document.addEventListener("DOMContentLoaded", function (event) {
        const mm = MetisMenu.attach('#side-mm', {
            preventDefault: true,
            activeClass: 'active'
        });
    });
};


function toggle(checkboxes_name, source) {
    const checkboxes = document.querySelectorAll(`[data-target="${checkboxes_name}"]`);

    if (checkboxes.length) {
        if (typeof source === 'undefined') initial_status = checkboxes[0].checked;
        else initial_status = !source.checked;

        for (var i in checkboxes) checkboxes[i].checked = !initial_status;
    }
}
