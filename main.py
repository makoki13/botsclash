from asciimatics.widgets import Frame, TextBox, Layout, Label, Divider, Text, \
    CheckBox, RadioButtons, Button, PopUpDialog
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication, \
    InvalidFields
import sys
import re

# Initial data for the form
form_data = {
    "TA": ["Hello world!", "How are you?"],
    "TB": "alphabet",
    "TC": "123",
    "TD": "a@b.com",
    "Things": 2,
    "CA": False,
    "CB": True,
    "CC": False,
}


class DemoFrame(Frame):
    def __init__(self, screen):
        super(DemoFrame, self).__init__(screen,
                                        int(screen.height),
                                        int(screen.width * 0.25),
                                        data=form_data,
                                        has_shadow=True,
                                        name="My Form")
        layout = Layout([1, 18, 1])
        self.add_layout(layout)
        self._reset_button = Button("Reset", self._reset)
        layout.add_widget(Label("Group 1:"), 1)
        layout.add_widget(TextBox(5,
                                  label="My First Box:",
                                  name="TA",
                                  on_change=self._on_change), 1)
        layout.add_widget(
            Text(label="Alpha:",
                 name="TB",
                 on_change=self._on_change,
                 validator="^[a-zA-Z]*$"), 1)
        layout.add_widget(
            Text(label="Number:",
                 name="TC",
                 on_change=self._on_change,
                 validator="^[0-9]*$"), 1)
        layout.add_widget(
            Text(label="Email:",
                 name="TD",
                 on_change=self._on_change,
                 validator=self._check_email), 1)
        layout.add_widget(Divider(height=2), 1)
        layout.add_widget(Label("Group 2:"), 1)
        layout.add_widget(RadioButtons([("Option 1", 1),
                                        ("Option 2", 2),
                                        ("Option 3", 3)],
                                       label="A Longer Selection:",
                                       name="Things",
                                       on_change=self._on_change), 1)
        layout.add_widget(CheckBox("Field 1",
                                   label="A very silly long name for fields:",
                                   name="CA",
                                   on_change=self._on_change), 1)
        layout.add_widget(
            CheckBox("Field 2", name="CB", on_change=self._on_change), 1)
        layout.add_widget(
            CheckBox("Field 3", name="CC", on_change=self._on_change), 1)
        layout.add_widget(Divider(height=3), 1)
        layout2 = Layout([1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(self._reset_button, 0)
        layout2.add_widget(Button("View Data", self._view), 1)
        layout2.add_widget(Button("Quit", self._quit), 2)
        self.fix()

    def _on_change(self):
        changed = False
        self.save()
        for key, value in self.data.items():
            if key not in form_data or form_data[key] != value:
                changed = True
                break
        self._reset_button.disabled = not changed

    def _reset(self):
        self.reset()
        raise NextScene()

    def _view(self):
        # Build result of this form and display it.
        try:
            self.save(validate=True)
            message = "Values entered are:\n\n"
            for key, value in self.data.items():
                message += "- {}: {}\n".format(key, value)
        except InvalidFields as exc:
            message = "The following fields are invalid:\n\n"
            for field in exc.fields:
                message += "- {}\n".format(field)
        self._scene.add_effect(
            PopUpDialog(self._screen, message, ["OK"]))

    def _quit(self):
        self._scene.add_effect(
            PopUpDialog(self._screen,
                        "Are you sure?",
                        ["Yes", "No"],
                        on_close=self._quit_on_yes))

    @staticmethod
    def _check_email(value):
        m = re.match(r"^[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z0-9_\-\.]+$",
                     value)
        return len(value) == 0 or m is not None

    @staticmethod
    def _quit_on_yes(selected):
        # Yes is the first button
        if selected == 0:
            raise StopApplication("User requested exit")

class DemoFrame2(Frame):
    def __init__(self, screen):
        super(DemoFrame2, self).__init__(screen,
                                        int(screen.height * 0.95),
                                        int(screen.width * 0.9),
                                        data=form_data,
                                        has_shadow=True,
                                        name="My Form")
        #layout = Layout([1, 18, 1])
        #self.add_layout(layout)
        layout = Layout([1, 3])
        self.add_layout(layout)

        layout.add_widget(Button("Añadir personaje", self._quit), 0)
        layout.add_widget(Button("Borrar personaje ", self._quit), 0)
        layout.add_widget(Button("Editar personaje", self._quit), 0)
        layout.add_widget(Button("Testear personajes", self._quit), 0)
        layout.add_widget(Button("Salir", self._quit), 0)

        self._reset_button = Button("Añadir personaje", self._reset)
        #layout.add_widget(self._reset_button, 0)
        #layout.add_widget(Button("Salir", self._quit), 0)
        layout.add_widget(Label("Group 1:"), 1)
        layout.add_widget(TextBox(5,
                                  label="My First Box:",
                                  name="TA",
                                  on_change=self._on_change), 1)
        layout.add_widget(
            Text(label="Alpha:",
                 name="TB",
                 on_change=self._on_change,
                 validator="^[a-zA-Z]*$"), 1)
        layout.add_widget(
            Text(label="Number:",
                 name="TC",
                 on_change=self._on_change,
                 validator="^[0-9]*$"), 1)
        layout.add_widget(
            Text(label="Email:",
                 name="TD",
                 on_change=self._on_change,
                 validator=self._check_email), 1)
        layout.add_widget(Divider(height=2), 1)
        layout.add_widget(Label("Group 2:"), 1)
        layout.add_widget(RadioButtons([("Option 1", 1),
                                        ("Option 2", 2),
                                        ("Option 3", 3)],
                                       label="A Longer Selection:",
                                       name="Things",
                                       on_change=self._on_change), 1)
        layout.add_widget(CheckBox("Field 1",
                                   label="A very silly long name for fields:",
                                   name="CA",
                                   on_change=self._on_change), 1)
        layout.add_widget(
            CheckBox("Field 2", name="CB", on_change=self._on_change), 1)
        layout.add_widget(
            CheckBox("Field 3", name="CC", on_change=self._on_change), 1)
        layout.add_widget(Divider(height=3), 1)
        layout2 = Layout([1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(self._reset_button, 0)
        layout2.add_widget(Button("View Data", self._view), 1)
        layout2.add_widget(Button("Quit", self._quit), 2)
        self.fix()

    def _on_change(self):
        changed = False
        self.save()
        for key, value in self.data.items():
            if key not in form_data or form_data[key] != value:
                changed = True
                break
        self._reset_button.disabled = not changed

    def _reset(self):
        self.reset()
        raise NextScene()

    def _view(self):
        # Build result of this form and display it.
        try:
            self.save(validate=True)
            message = "Values entered are:\n\n"
            for key, value in self.data.items():
                message += "- {}: {}\n".format(key, value)
        except InvalidFields as exc:
            message = "The following fields are invalid:\n\n"
            for field in exc.fields:
                message += "- {}\n".format(field)
        self._scene.add_effect(
            PopUpDialog(self._screen, message, ["OK"]))

    def _quit(self):
        self._scene.add_effect(
            PopUpDialog(self._screen,
                        "Are you sure?",
                        ["Yes", "No"],
                        on_close=self._quit_on_yes))

    @staticmethod
    def _check_email(value):
        m = re.match(r"^[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z0-9_\-\.]+$",
                     value)
        return len(value) == 0 or m is not None

    @staticmethod
    def _quit_on_yes(selected):
        # Yes is the first button
        if selected == 0:
            raise StopApplication("User requested exit")

def demo(screen, scene):
    scenes = []
    #scenes.append(Scene([DemoFrame(screen)], -1))
    scenes.append(Scene([DemoFrame2(screen)], -1))
    screen.play(scenes, stop_on_resize=True, start_scene=scene)

last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=False, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene