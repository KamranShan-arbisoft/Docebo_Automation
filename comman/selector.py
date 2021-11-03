class LoginPageSelectors:
    name = '.login-field-username>div>div:nth-child(1)>div>input'
    password = '.login-field-password>div>div:nth-child(1)>input'


class NewUSerSelectors:
    admin_menu = 'button[aria-label="Admin Menu"]'
    user = 'a[id="item_00"]'
    new_user = 'button[aria-label="New Users"]'
    visible_new_user = 'button[aria-label="New user"]'
    user_name = 'input[id="username_field"]'
    user_email = 'input[id="email_field"]'
    user_first_name = 'input[id="firstname_field"]'
    user_last_name = 'input[id="lastname_field"]'
    email_validation_drop = 'div[aria-label="Email Validation Status"]>span:nth-child(2)'
    email_validation_item = 'div[id="dropdown-body-field-2"]>div.dropdown-items>ul>li:nth-child(2)'
    next_button = 'button.next-button'
    all_branch = 'div.user-branches div.mdl-textfield-holder>span.dropdown-icon'
    branch_item = '.form-search-body.bg-white.dropdown-opened>ul>li:nth-child(1)'
    client_name = 'input[id="1"]'
    client_id = 'input[id="2"]'
    wave_cohort = 'textarea[id="textarea-mdl"]'
    primary_experience_drop = 'div[aria-label="Primary Experience"]'
    primary_experience_item = 'div[id="dropdown-body-field-5"]>div.dropdown-items>ul>li:nth-child(4)'
    group_work = 'input[id="14"]'
    custom_field1 = 'textarea[name="additionalField-16"]'
    custom_field2 = 'textarea[name="additionalField-17"]'
    custom_field3 = 'textarea[name="additionalField-18"]'
    custom_field4 = 'textarea[name="additionalField-19"]'
    m_info = 'auto-complete[id="manager_1"] input.mdl-textfield__input'
    preview_btn = 'div.users-rightpanel div[role="dialog"]>div>footer>basic-button:nth-child(3)>button'
    create_user_button = 'div.users-rightpanel div[role="dialog"]>div>footer>basic-button:nth-child(1)>button'
    search_input = 'input[id="search-1"]'
    search_btn = 'button[for="search-1"]'
