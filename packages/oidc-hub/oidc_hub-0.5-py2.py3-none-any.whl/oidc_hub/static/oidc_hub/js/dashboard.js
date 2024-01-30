/**
 * This function runs when the DOM and every stylesheets, scripts and external
 * resources have been loaded.
 */
window.onload = () => {
  // retrieve the add invitation button
  // if (user.is_superuser) {
    const add_invitation = document.querySelector('#add-invitation');
    const modal = document.querySelector('#modal-invitation');
    const close_modal = modal.querySelector('div.modal-content svg');
    add_invitation.addEventListener('click', () => { modal.style.visibility = "visible"; });
    close_modal.addEventListener('click', () => { modal.style.visibility = "hidden"; });

    // checkboxes
    const topCheckbox = document.querySelector('#check-all');
    const nodes = document.querySelectorAll('input[type="checkbox"]:not(#check-all)');
    
    // store the checkbox elements in an array
    const checkboxes = Array.from(nodes);

    // function to handle checkbox change event
    const checkboxChangeHandler = () => {
      // check if any checkbox is checked
      const any = checkboxes.some(checkbox => checkbox.checked);
      // check if all checkboxes are checked
      const all = checkboxes.every(checkbox => checkbox.checked);      
      // set indeterminate state based on checkbox states
      topCheckbox.checked = all;
      topCheckbox.indeterminate = any && !all;
    };

    topCheckbox.addEventListener('change', () => {
      checkboxes.forEach(checkbox => {
        checkbox.checked = topCheckbox.checked;
      });
    });

    checkboxes.forEach(checkbox => {
      checkbox.addEventListener('change', checkboxChangeHandler);
    });

  // }
    const action_submit = document.querySelector(".actions .checked button[type='submit']");
    const action_select = document.querySelector("select[form='selection']");
    action_select.addEventListener('change', () => {
      action_submit.disabled = false;
    });
};
