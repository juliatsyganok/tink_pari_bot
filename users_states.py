from aiogram.filters.state import State, StatesGroup

class UserStates(StatesGroup):
    BASE = State()
    CREATE_PARI = State()