[![github](https://img.shields.io/badge/my_profile-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Daxexs)[![pypi](https://img.shields.io/badge/Pypi-0A66C2?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/flet-easy)

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm-project.org)

<div align="center">
    <img src="https://raw.githubusercontent.com/Daxexs/flet-easy/main/media/logo.png" alt="logo" width="250">
</div>


# 🔥Flet-Easy
`Flet-Easy` is a package built as an add-on for [`Flet`](https://github.com/flet-dev/flet), designed for beginners what it does is to make `Flet` easier when building your apps, with a tidier and simpler code. Some functions:

* Facilitates the handling of flet events.
* Page building using decorators, which allows you to make numerous custom configurations to flet for desktop, mobile and website application.
* Designed to work with numerous pages of your created application.
* Provides better MVC construction of your code, which can be scalable and easy to read.
* Not only limits the MVC model but you can customize it according to your preferences.
* Customized URLs for more precision in sending data.
* Support asynchronous.
* Supports Application Packaging for distribution.

## 📌Flet events it handles

- `on_route_change` :  Dynamic routing
- `on_view_pop`
- `on_keyboard_event`
- `on_resize`
- `on_error`

## 📌Form of use:
- Installation [view](#Installation)
- Flet-Easy app example [view](#Flet-Easy-app-example)
- How to use Flet-Easy? [view](#-How-to-use-Flet-Easy)
- How to create a new page? [view](#-How-to-create-a-new-page)
- Using dynamic routes [view](#-Using-Dynamic-Routes)
- Add pages from other files to the main application. [view](#-add-pages-from-other-files-to-the-main-application)
- Adding pages to the main app without using decorators [view](#-Adding-pages-to-the-main-app-without-using-decorators)
- Customized app configuration [view](#-Customized-app-configuration)
  - Route protection [view](#-Route-protection)
  - Add general settings in the app. [view](#%EF%B8%8F-add-general-settings-in-the-app)
  - Add settings of the View controller of Flet [view](#-Add-settings-of-the-View-controller-of-Flet)
  - Add a custom page, which will be activated when a page (path) is not found. [view](#%EF%B8%8F-add-a-custom-page-which-will-be-activated-when-a-page-path-is-not-found)
  - Configure custom events [view](#-configure-custom-events)
- Events configured by Flet-Easy. [view](#-events-configured-by-flet-easy)
  - Use on_keyboard_event [view](#%EF%B8%8F-use-on_keyboard_event)
  - Use on_resize [view](#%EF%B8%8F-use-on_resize)
- Class ResponsiveControlsy [view](#-Class-ResponsiveControlsy)
- Run the app [view](#-Run-the-app)
- Working with other apps and creating apis [view](-working-with-other-apps-and-creating-apis)
- Code examples [view](-code-examples)


## 💻Installation:
Requires installation for use:
* Flet (Installed automatically)
* Flet-fastapi (Optional)
* uvicorn (Optional)
```bash
  pip install flet-easy
```

## 💻Update:
```bash
  pip install flet-easy --upgrade
```

## 🔥Flet-Easy app example
Here is an example of an application with 2 pages, "Home" and "Counter":

```python
import flet as ft
import flet_easy as fs

app = fs.FletEasy(route_init="/flet-easy")

# We add a page
@app.page(route="/flet-easy")
def index_page(data: fs.Datasy):
    page = data.page

    page.title = "Flet-Easy"

    def go_counter(e):
        page.go("/counter")

    return ft.View(
        route="/flet-easy",
        controls=[
            ft.Text("Home page"),
            ft.FilledButton("Go to Counter", on_click=go_counter),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

# We add a second page
@app.page(route="/counter")
def counter_page(data: fs.Datasy):
    page = data.page

    page.title = "Counter"

    txt_number = ft.TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def go_home(e):
        page.go("/flet-easy")

    return ft.View(
        route="/counter",
        controls=[
            ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                    txt_number,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ],
                alignment="center",
            ),
            ft.FilledButton("Go to Home", on_click=go_home),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

# We run the application
app.run()
```
### 🔎 More information [here](https://github.com/Daxexs/flet-easy)