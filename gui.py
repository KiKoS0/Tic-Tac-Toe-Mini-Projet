from kivy.app import App
from kivy.properties import OptionProperty, NumericProperty, ListProperty, \
        BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.lang import Builder
from kivy.clock import Clock
from math import cos, sin

Builder.load_string('''
<LinePlayground>:
    canvas.before:
        Color:
            rgba: 0.14, 0.14, 0.14, 1
        Rectangle:
            pos: self.pos
            size: self.size
    GridLayout:
        cols: 2
        size_hint: 1, None
        height: 44 * 5

        GridLayout:
            id: parent_layout
            cols: 2

            Label:
                text: 'Mode de jeu (contre)'
            GridLayout:
                cols: 4
                Label:
                    text: 'Ordinateur'
                CheckBox:
                    allow_no_selection: False
                    group: 'gamemode' 
                    active: True
                    on_state: root.AiActivated = True; root.stateChange();root.toogleAiInput(False)
                Label:
                    text: 'Joueur'
                CheckBox:
                    allow_no_selection: False
                    group: 'gamemode'
                    on_state: root.AiActivated = False; root.stateChange();root.toogleAiInput(True)
            
            Label:
                text: 'Pion joueur 1'
            GridLayout:
                cols: 4
                Label:
                    text: 'X'
                CheckBox:
                    allow_no_selection: False
                    group: 'pion' 
                    active: True
                    on_state: root.pion = 'X'
                Label:
                    text: 'O'
                CheckBox:
                    allow_no_selection: False
                    group: 'pion'
                    on_state: root.pion = 'O'
            
            Label:
                id: player_label
                text: 'Player Name'
            TextInput:
                text: ''
                multiline: False
            Label:
                id: player_label
                text: 'Player 2 Name'
                disabled: True
            TextInput:
                id: player_input
                text: 'Colosse'
                multiline: False
                disabled: True
            Label:
                id: diff_label
                text: 'Difficulte'
            GridLayout:
                id: diff_layout
                cols: 4
                Label:
                    text: 'Normale'
                CheckBox:
                    allow_no_selection: False
                    group: 'difficulty' 
                    active: True
                    on_state: root.AiDifficult = False; root.stateChange()
                Label:
                    text: 'Imbattable'
                CheckBox:
                    allow_no_selection: False
                    group: 'difficulty'
                    on_state: root.AiDifficult = True; root.stateChange()

        AnchorLayout:
            GridLayout:
                cols: 1
                size_hint: None, None
                size: self.minimum_size
                ToggleButton:
                    size_hint: None, None
                    size: 100, 44
                    text: 'Jouer'
                    on_state: root.animate(self.state == 'down')
                Button:
                    size_hint: None, None
                    size: 100, 44
                    text: 'Quitter'
                    on_press: quit()

''')


class LinePlayground(AnchorLayout):
    AiActivated = True
    AiDifficult = False
    pion = 'X'
    def toogleAiInput(self,state):
        self.ids.diff_layout.disabled = state
        self.ids.player_input.text = "Colosse"
        self.ids.player_label.disabled = not state
        self.ids.player_input.disabled = not state

    def stateChange(self):
        print('Ai activation : ' + str(self.AiActivated))
        print('Ai difficult : ' + str(self.AiDifficult))
    def toogleAI(self):
        self.AiActivated = True if not self.AiActivated else False
        print('Ai activation : '+str(self.AiActivated))
    def toogleAIDifficulty(self):
        self.AiDifficult = True if not self.AiDifficult else False
        print('Ai difficult : '+str(self.AiDifficult))

    #alpha_controlline = NumericProperty(1.0)
    #alpha = NumericProperty(0.5)
    #close = BooleanProperty(False)
    # points = ListProperty([(500, 500),
    #                       [300, 300, 500, 300],
    #                       [500, 400, 600, 400]])
    # points2 = ListProperty([])
    # joint = OptionProperty('none', options=('round', 'miter', 'bevel', 'none'))
    # cap = OptionProperty('none', options=('round', 'square', 'none'))
    linewidth = NumericProperty(10.0)
    # dt = NumericProperty(0)

    # _update_points_animation_ev = None

    # def on_touch_down(self, touch):
    #     if super(LinePlayground, self).on_touch_down(touch):
    #         return True
    #     touch.grab(self)
    #     self.points.append(touch.pos)
    #     return True
    #
    # def on_touch_move(self, touch):
    #     if touch.grab_current is self:
    #         self.points[-1] = touch.pos
    #         return True
    #     return super(LinePlayground, self).on_touch_move(touch)
    #
    # def on_touch_up(self, touch):
    #     if touch.grab_current is self:
    #         touch.ungrab(self)
    #         return True
    #     return super(LinePlayground, self).on_touch_up(touch)
    #
    # def animate(self, do_animation):
    #     if do_animation:
    #         self._update_points_animation_ev = Clock.schedule_interval(
    #             self.update_points_animation, 0)
    #     elif self._update_points_animation_ev is not None:
    #         self._update_points_animation_ev.cancel()
    #
    # def update_points_animation(self, dt):
    #     cy = self.height * 0.6
    #     cx = self.width * 0.1
    #     w = self.width * 0.8
    #     step = 20
    #     points = []
    #     points2 = []
    #     self.dt += dt
    #     for i in range(int(w / step)):
    #         x = i * step
    #         points.append(cx + x)
    #         points.append(cy + cos(x / w * 8. + self.dt) * self.height * 0.2)
    #         points2.append(cx + x)
    #         points2.append(cy + sin(x / w * 8. + self.dt) * self.height * 0.2)
    #     self.points = points
    #     self.points2 = points2


class TestLineApp(App):
    def build(self):
        return LinePlayground()


if __name__ == '__main__':
    TestLineApp().run()