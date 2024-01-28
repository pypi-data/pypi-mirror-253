import streamlit.components.v1 as components
import os


_RELEASE = True


if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "st_comments",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3000",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_comments", path=build_dir)

def st_comments(comments,delete_keyword="", max_height="500px",custom_css="",key="st_comments",min_height="100px",
                custom_font_awesome_url = "https://kit.fontawesome.com/c7cbba6207.js", delete_user="all",return_mode = "all",auth_token:str = None, host_url_api = None, textfield=False,
                api_user_name = "",max_chars = 1000, button_post_label="Post",text_field_placeholder=None, submitButtonColor="#1E90FF",comment_field_key=None, new_on_top=True,
                allow_html_comment = True, retrieve_from_api = False, no_comments_text = "No Comments yet"):
    """
    Component um Kommetare anzuzeigen zu löschen und zubearbeiten

    Parameters

    ----------

    comments : list
        Liste mit Kommentaren in Form von Dictionaries. Jedes Dictionary muss die Keys "id", "user", "date" und "text" enthalten.
    delete_keyword : str (Kann auch HTML sein)
        Keyword um Kommentare zu löschen. Standard ist "Delete". Wenn HTML verwendet wird, muss das Keyword in Anführungszeichen stehen.
    max_height : str
        Maximale Höhe des Components. Standard ist "500px".
    min_height : str
        Minimale Höhe des Components. Standard ist "100px".
    custom_css : str
        Custom CSS für den Component. Standard ist "".
    key : str
        Key für den Component. Standard ist "st_comments".
    custom_font_awesome_url : str
        URL für die Font Awesome Bibliothek. Standard ist "https://kit.fontawesome.com/c7cbba6207.js".
    delete_user : str
        Controls wether someone is allowed to delete all comments or only his own. Standard is "all". Other option is is the Name of the user (each name should be unique ;) or "none" if no deletion is allowed.
    return_mode : str
        all, deleted, none, api 
    auth_token : str
        Authentifizierungstoken für die API
    host_url_api : str
        URL für die API
    textfield : bool
        Controls wether a textfield for new comments is shown or not. Standard is False.
    api_user_name : str
        Name des Users der die API verwendet
    max_chars : int
        Maximale Anzahl an Zeichen für einen Kommentar. Standard ist 1000.
    button_post_label : str
        Label für den Post Button. Standard ist "Post".
    text_field_placeholder : str
        Placeholder für das Textfeld. Standard ist None.
    new_on_top : bool
        Controls wether new comments are shown on top or on bottom. Standard is False.
    allow_html_comment : bool
        Controls wether HTML is allowed in comments. Standard is True.
    retrieve_from_api : bool
        Controls wether comments are retrieved from the API. Standard is False.
    no_comments_text : str
        Text der angezeigt wird wenn keine Kommentare vorhanden sind. Standard ist "No Comments yet".
    """
    if return_mode == "api":
        if comment_field_key == None:
            raise ValueError("comment_field_key must be set if return_mode is api")
    if return_mode == "all":
        default_value = comments
    else:
        default_value = []
       
    component_value = _component_func(comments=comments, delete_keyword=delete_keyword, max_height=max_height, custom_css=custom_css, key=key,min_height= min_height,
                                      custom_font_awesome_url = custom_font_awesome_url, delete_user = delete_user, return_mode = return_mode, default= default_value,
                                      auth_token = auth_token, host_url_api = host_url_api,textfield=textfield,api_user_name=api_user_name, max_chars = max_chars,
                                      button_post_label=button_post_label,text_field_placeholder=text_field_placeholder,submitButtonColor=submitButtonColor,comment_field_key=comment_field_key,
                                      new_on_top=new_on_top, allow_html_comment = allow_html_comment,retrieve_from_api = retrieve_from_api,
                                      no_comments_text = no_comments_text)
                                    

    if return_mode  in ["none","api"]:
        pass
    else:
        return component_value
