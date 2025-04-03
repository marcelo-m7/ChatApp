import flet as ftdef main(page: ft.Page):    page.add(ft.Text(value="Hello, world!"))ft.app(main)

import flet as ftdef main(page: ft.Page):    card = ft.GestureDetector(       left=0,       top=0,       content=ft.Container(bgcolor=ft.Colors.GREEN, width=70, height=100),   )       page.add(ft.Stack(controls=[card], width=1000, height=500)) ft.app(main)

import flet as ft # Use of GestureDetector for with on_pan_update event for dragging card# Absolute positioning of controls within stack def main(page: ft.Page):    def drag(e: ft.DragUpdateEvent):       e.control.top = max(0, e.control.top + e.delta_y)       e.control.left = max(0, e.control.left + e.delta_x)       e.control.update()    card = ft.GestureDetector(       mouse_cursor=ft.MouseCursor.MOVE,       drag_interval=5,       on_pan_update=drag,       left=0,       top=0,       content=ft.Container(bgcolor=ft.Colors.GREEN, width=70, height=100),   )       page.add(ft.Stack(controls=[card], width=1000, height=500)) ft.app(main)

slot = ft.Container(    width=70, height=100, left=200, top=0, border=ft.border.all(1)    )page.add(ft.Stack(controls = [slot, card], width=1000, height=500))

card = ft.GestureDetector(    mouse_cursor=ft.MouseCursor.MOVE,    drag_interval=5,    on_pan_update=drag,    on_pan_end=drop,    left=0,    top=0,    content=ft.Container(bgcolor=ft.Colors.GREEN, width=70, height=100),)

def drop(e: ft.DragEndEvent):    if (        abs(e.control.top - slot.top) < 20        and abs(e.control.left - slot.left) < 20    ):        place(e.control, slot)    e.control.update()def place(card, slot):    """place card to the slot"""    card.top = slot.top    card.left = slot.left    page.update()

class Solitaire:   def __init__(self):       self.start_top = 0       self.start_left = 0solitaire = Solitaire()def start_drag(e: ft.DragStartEvent):    solitaire.start_top = e.control.top    solitaire.start_left = e.control.left    e.control.update()

def bounce_back(game, card):    """return card to its original position"""    card.top = game.start_top    card.left = game.start_left    page.update()def drop(e: ft.DragEndEvent):    if (        abs(e.control.top - slot.top) < 20        and abs(e.control.left - slot.left) < 20    ):        place(e.control, slot)    else:        bounce_back(solitaire, e.control)    e.control.update()

card2 = ft.GestureDetector(       mouse_cursor=ft.MouseCursor.MOVE,       drag_interval=5,       on_pan_start=start_drag,       on_pan_update=drag,       on_pan_end=drop,       left=100,       top=0,       content=ft.Container(bgcolor=ft.Colors.YELLOW, width=70, height=100),   )   controls = [slot, card1, card2]   page.add(ft.Stack(controls=controls, width=1000, height=500))

def move_on_top(card, controls):    """Moves draggable card to the top of the stack"""    controls.remove(card)    controls.append(card)    page.update()def start_drag(e: ft.DragStartEvent):    move_on_top(e.control, controls)    solitaire.start_top = e.control.top    solitaire.start_left = e.control.left

slot0 = ft.Container(    width=70, height=100, left=0, top=0, border=ft.border.all(1))slot1 = ft.Container(    width=70, height=100, left=200, top=0, border=ft.border.all(1))slot2 = ft.Container(    width=70, height=100, left=300, top=0, border=ft.border.all(1))slots = [slot0, slot1, slot2]

# deal cardsplace(card1, slot0)place(card2, slot0)

def drop(e: ft.DragEndEvent):    for slot in slots:        if (            abs(e.control.top - slot.top) < 20        and abs(e.control.left - slot.left) < 20        ):            place(e.control, slot)            e.control.update()            return            bounce_back(solitaire, e.control)    e.control.update()

SLOT_WIDTH = 70SLOT_HEIGHT = 100 import flet as ft class Slot(ft.Container):   def __init__(self, top, left):       super().__init__()       self.pile=[]       self.width=SLOT_WIDTH       self.height=SLOT_HEIGHT       self.left=left       self.top=top       self.border=ft.border.all(1)

CARD_WIDTH = 70CARD_HEIGTH = 100DROP_PROXIMITY = 20 import flet as ft class Card(ft.GestureDetector):   def __init__(self, solitaire, color):       super().__init__()       self.slot = None       self.mouse_cursor=ft.MouseCursor.MOVE       self.drag_interval=5       self.on_pan_start=self.start_drag       self.on_pan_update=self.drag       self.on_pan_end=self.drop       self.left=None       self.top=None       self.solitaire = solitaire       self.color = color       self.content=ft.Container(bgcolor=self.color, width=CARD_WIDTH, height=CARD_HEIGTH)      def move_on_top(self):       """Moves draggable card to the top of the stack"""       self.solitaire.controls.remove(self)       self.solitaire.controls.append(self)       self.solitaire.update()    def bounce_back(self):       """Returns card to its original position"""       self.top = self.slot.top       self.left = self.slot.left       self.update()    def place(self, slot):       """Place card to the slot"""       self.top = slot.top       self.left = slot.left    def start_drag(self, e: ft.DragStartEvent):       self.move_on_top()       self.update()    def drag(self, e: ft.DragUpdateEvent):       self.top = max(0, self.top + e.delta_y)       self.left = max(0, self.left + e.delta_x)       self.update()    def drop(self, e: ft.DragEndEvent):       for slot in self.solitaire.slots:           if (               abs(self.top - slot.top) < DROP_PROXIMITY           and abs(self.left - slot.left) < DROP_PROXIMITY         ):               self.place(slot)               self.update()               return                self.bounce_back()       self.update()

SOLITAIRE_WIDTH = 1000SOLITAIRE_HEIGHT = 500 import flet as ftfrom slot import Slotfrom card import Card class Solitaire(ft.Stack):   def __init__(self):       super().__init__()       self.controls = []       self.slots = []       self.cards = []       self.width = SOLITAIRE_WIDTH       self.height = SOLITAIRE_HEIGHT    def did_mount(self):       self.create_card_deck()       self.create_slots()       self.deal_cards()    def create_card_deck(self):       card1 = Card(self, color="GREEN")       card2 = Card(self, color="YELLOW")       self.cards = [card1, card2]    def create_slots(self):       self.slots.append(Slot(top=0, left=0))       self.slots.append(Slot(top=0, left=200))       self.slots.append(Slot(top=0, left=300))       self.controls.extend(self.slots)       self.update()    def deal_cards(self):       self.controls.extend(self.cards)       for card in self.cards:           card.place(self.slots[0])       self.update()

import flet as ftfrom solitaire import Solitaire def main(page: ft.Page):     solitaire = Solitaire()    page.add(solitaire) ft.app(main)

def place(self, slot):    # remove card from it's original slot, if exists    if self.slot is not None:        self.slot.pile.remove(self)        # change card's slot to a new slot    self.slot = slot    # add card to the new slot's pile    slot.pile.append(self)

self.top = slot.top + len(slot.pile) * CARD_OFFSET    self.left = slot.left

def get_draggable_pile(self):        """returns list of cards that will be dragged together, starting with the current card"""        if self.slot is not None:            self.draggable_pile = self.slot.pile[self.slot.pile.index(self) :]        else:  # slot == None when the cards are dealt and need to be place in slot for the first time            self.draggable_pile = [self]

def move_on_top(self):        """Brings draggable card pile to the top of the stack"""        # for card in self.get_draggable_pile():        for card in self.draggable_pile:            self.solitaire.controls.remove(card)            self.solitaire.controls.append(card)        self.solitaire.update()

def drag(self, e: ft.DragUpdateEvent):        for card in self.draggable_pile:            card.top = (                max(0, self.top + e.delta_y)                + self.draggable_pile.index(card) * CARD_OFFSET            )            card.left = max(0, self.left + e.delta_x)            self.solitaire.update()

def place(self, slot):        """Place draggable pile to the slot"""        for card in self.draggable_pile:            card.top = slot.top + len(slot.pile) * CARD_OFFSET            card.left = slot.left            # remove card from it's original slot, if it exists            if card.slot is not None:                card.slot.pile.remove(card)            # change card's slot to a new slot            card.slot = slot            # add card to the new slot's pile            slot.pile.append(card)        self.solitaire.update()

def bounce_back(self):        """Returns draggable pile to its original position"""        for card in self.draggable_pile:            card.top = card.slot.top + card.slot.pile.index(card) * CARD_OFFSET            card.left = card.slot.left        self.solitaire.update()

class Suite:    def __init__(self, suite_name, suite_color):        self.name = suite_name        self.color = suite_colorclass Rank:    def __init__(self, card_name, card_value):        self.name = card_name        self.value = card_value

class Card(ft.GestureDetector):    def __init__(self, solitaire, suite, rank):        super().__init__()        self.mouse_cursor=ft.MouseCursor.MOVE        self.drag_interval=5        self.on_pan_start=self.start_drag        self.on_pan_update=self.drag        self.on_pan_end=self.drop        self.suite=suite        self.rank=rank        self.face_up=False        self.top=None        self.left=None        self.solitaire = solitaire        self.slot = None        self.content=ft.Container(            width=CARD_WIDTH,            height=CARD_HEIGTH,            border_radius = ft.border_radius.all(6),            content=ft.Image(src="card_back.png"))

ft.app(main, assets_dir="images")

def create_card_deck(self):    suites = [        Suite("hearts", "RED"),        Suite("diamonds", "RED"),        Suite("clubs", "BLACK"),        Suite("spades", "BLACK"),    ]    ranks = [        Rank("Ace", 1),        Rank("2", 2),        Rank("3", 3),        Rank("4", 4),        Rank("5", 5),        Rank("6", 6),        Rank("7", 7),        Rank("8", 8),        Rank("9", 9),        Rank("10", 10),        Rank("Jack", 11),        Rank("Queen", 12),        Rank("King", 13),    ]    self.cards = []    for suite in suites:        for rank in ranks:            self.cards.append(Card(solitaire=self, suite=suite, rank=rank))

def create_slots(self):        self.stock = Slot(top=0, left=0, border=ft.border.all(1))    self.waste = Slot(top=0, left=100, border=None)    self.foundations = []    x = 300    for i in range(4):        self.foundations.append(Slot(top=0, left=x, border=ft.border.all(1, "outline")))        x += 100    self.tableau = []    x = 0    for i in range(7):        self.tableau.append(Slot(top=150, left=x, border=None))        x += 100    self.controls.append(self.stock)    self.controls.append(self.waste)    self.controls.extend(self.foundations)    self.controls.extend(self.tableau)    self.update()

def deal_cards(self):    random.shuffle(self.cards)    self.controls.extend(self.cards)    self.update()

def deal_cards(self):    random.shuffle(self.cards)    self.controls.extend(self.cards)        # deal to tableau    first_slot = 0    remaining_cards = self.cards        while first_slot < len(self.tableau):        for slot in self.tableau[first_slot:]:            top_card = remaining_cards[0]            top_card.place(slot)            remaining_cards.remove(top_card)        first_slot +=1    # place remaining cards to stock pile    for card in remaining_cards:        card.place(self.stock)        self.update()

def place(self, slot):    """Place draggable pile to the slot"""    if slot in self.solitaire.tableau:        self.top = slot.top + len(slot.pile) * self.solitaire.card_offset    else:        self.top = slot.top    self.left = slot.left

def drop(self, e: ft.DragEndEvent):    for slot in self.solitaire.tableau:        if (            abs(self.top - (slot.top + len(slot.pile) * CARD_OFFSET)) < DROP_PROXIMITY        and abs(self.left - slot.left) < DROP_PROXIMITY        ):            self.place(slot)            self.solitaire.update()            return    for slot in self.solitaire.foundations:        if (            abs(self.top - slot.top) < DROP_PROXIMITY        and abs(self.left - slot.left) < DROP_PROXIMITY        ):            self.place(slot)            self.solitaire.update()            return            self.bounce_back()

def get_top_card(self):    if len(self.pile) > 0:        return self.pile[-1]

def turn_face_up(self):    self.face_up = True    self.content.content.src=f"/images/{self.rank.name}_{self.suite.name}.svg"    self.solitaire.update()

for slot in self.tableau:    slot.get_top_card().turn_face_up()    self.update()

def start_drag(self, e: ft.DragStartEvent):    if self.face_up:        self.move_on_top()        self.solitaire.update()def drag(self, e: ft.DragUpdateEvent):    if self.face_up:        for card in self.draggable_pile:            card.top = max(0, self.top + e.delta_y) + self.draggable_pile.index(card) * CARD_OFFSET            card.left = max(0, self.left + e.delta_x)            card.solitaire.update()def drop(self, e: ft.DragEndEvent):    if self.face_up:        for slot in self.solitaire.tableau:            if (                abs(self.top - (slot.top + len(slot.pile) * CARD_OFFSET)) < DROP_PROXIMITY            and abs(self.left - slot.left) < DROP_PROXIMITY        ):                self.place(slot)                return                for slot in self.solitaire.foundations:            if (                    abs(self.top - slot.top) < DROP_PROXIMITY            and abs(self.left - slot.left) < DROP_PROXIMITY        ):                self.place(slot)                return            self.bounce_back()

def click(self, e):    if self.slot in self.solitaire.tableau:        if not self.face_up and self == self.slot.get_top_card():            self.turn_face_up()            self.solitaire.update()

def drop(self, e: ft.DragEndEvent):    for slot in self.solitaire.tableau:        if (            abs(self.top - (slot.top + len(slot.pile) * CARD_OFFSET)) < DROP_PROXIMITY        and abs(self.left - slot.left) < DROP_PROXIMITY        ):            self.place(slot)            return        if len(self.draggable_pile) == 1:        for slot in self.solitaire.foundations:            if (                abs(self.top - slot.top) < DROP_PROXIMITY        and abs(self.left - slot.left) < DROP_PROXIMITY        ):                self.place(slot)                return            self.bounce_back()

def check_foundations_rules(self, card, slot):    top_card = slot.get_top_card()    if top_card is not None:        return (            card.suite.name == top_card.suite.name            and card.rank.value - top_card.rank.value == 1        )    else:        return card.rank.name == "Ace"

def drop(self, e: ft.DragEndEvent):    if self.face_up:        for slot in self.solitaire.tableau:            if (                abs(self.top - (slot.top + len(slot.pile) * CARD_OFFSET)) < DROP_PROXIMITY            and abs(self.left - slot.left) < DROP_PROXIMITY        ):                self.place(slot)                return                if len(self.draggable_pile) == 1:            for slot in self.solitaire.foundations:                if (                    abs(self.top - slot.top) < DROP_PROXIMITY            and abs(self.left - slot.left) < DROP_PROXIMITY        ) and self.solitaire.check_foundations_rules(self, slot):                    self.place(slot)                    return                self.bounce_back()

def double-click(self, e):       self.get_draggable_pile()       if self.face_up and len(self.draggable_pile == 1):           self.move_on_top()           for slot in self.solitaire.foundations:               if self.solitaire.check_foundations_rules(self, slot):                   self.place(slot)                   return

def check_tableau_rules(self, card, slot):    top_card = slot.get_top_card()    if top_card is not None:        return (            card.suite.color != top_card.suite.color            and top_card.rank.value - card.rank.value == 1            and top_card.face_up        )    else:        return card.rank.name == "King"

def drop(self, e: ft.DragEndEvent):    if self.face_up:        for slot in self.solitaire.tableau:            if (                abs(self.top - (slot.top + len(slot.pile) * CARD_OFFSET)) < DROP_PROXIMITY            and abs(self.left - slot.left) < DROP_PROXIMITY        ) and self.solitaire.check_tableau_rules(self, slot):                self.place(slot)                return                if len(self.draggable_pile) == 1:            for slot in self.solitaire.foundations:                if (                    abs(self.top - slot.top) < DROP_PROXIMITY            and abs(self.left - slot.left) < DROP_PROXIMITY        ) and self.solitaire.check_foundations_rules(self, slot):                    self.place(slot)                    return                self.bounce_back()

def click(self, e):    if self.slot in self.solitaire.tableau:        if not self.face_up and self == self.slot.get_top_card():            self.turn_face_up()    elif self.slot == self.solitaire.stock:        self.move_on_top()        self.place(self.solitaire.waste)        self.turn_face_up()

class Slot(ft.Container):   def __init__(self, solitaire, top, left, border):       super().__init__()       self.pile=[]       self.width=SLOT_WIDTH       self.height=SLOT_HEIGHT       self.left=left       self.top=top       self.on_click=self.click       self.solitaire=solitaire       self.border=border       self.border_radius = ft.border_radius.all(6)     def click(self, e):       if self == self.solitaire.stock:           self.solitaire.restart_stock()

def restart_stock(self):    while len(self.waste.pile) > 0:        card = self.waste.get_top_card()        card.turn_face_down()        card.move_on_top()        card.place(self.stock)

def get_draggable_pile(self):        """returns list of cards that will be dragged together, starting with the current card"""        if (            self.slot is not None            and self.slot != self.solitaire.stock            and self.slot != self.solitaire.waste        ):            self.draggable_pile = self.slot.pile[self.slot.pile.index(self) :]        else:  # slot == None when the cards are dealt and need to be place in slot for the first time            self.draggable_pile = [self]

def check_win(self):    cards_num = 0    for slot in self.foundations:        cards_num += len(slot.pile)    if cards_num == 52:        return True    return False

def place(self, slot):    """Place draggable pile to the slot"""        draggable_pile = self.get_draggable_pile()    for card in draggable_pile:        if slot in self.solitaire.tableau:            card.top = slot.top + len(slot.pile) * CARD_OFFSET        else:            card.top = slot.top        card.left = slot.left        # remove card from it's original slot, if exists        if card.slot is not None:            card.slot.pile.remove(card)            # change card's slot to a new slot        card.slot = slot        # add card to the new slot's pile        slot.pile.append(card)        if self.solitaire.check_win():        self.solitaire.winning_sequence()        self.solitaire.update()

def winning_sequence(self):    for slot in self.foundations:           for card in slot.pile:            card.animate_position=1000            card.move_on_top()            card.top = random.randint(0, SOLITAIRE_HEIGHT)            card.left = random.randint(0, SOLITAIRE_WIDTH)            self.update()    self.controls.append(ft.AlertDialog(title=ft.Text("Congratulations! You won!"), open=True))

