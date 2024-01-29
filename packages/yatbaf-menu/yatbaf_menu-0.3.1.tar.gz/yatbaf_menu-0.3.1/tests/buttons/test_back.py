import pytest

from yatbaf.types import InlineKeyboardButton
from yatbaf_menu import Back
from yatbaf_menu import Menu


def test_init_no_parent(router, payload):
    menu = Menu(
        title="menu",
        name="menu",
        buttons=[
            button := Back(title="Back"),
        ],
    )
    button._init(menu, router, payload)
    assert not button._visible


def test_init(router, prefix, payload):
    menu = Menu(
        title="menu",
        name="menu",
        submenu=[
            submenu := Menu(
                title="submenu",
                name="submenu",
                buttons=[
                    button := Back(title="back"),
                ],
            ),
        ],
        back_btn_title="back",
    )
    menu._prefix = prefix
    submenu._parent = menu
    button._init(submenu, router, payload)
    assert button._payload == f"{menu._prefix}##"


def test_init_duplicate(router, payload):
    menu = Menu(
        title="menu",
        name="menu",
        submenu=[
            submenu := Menu(
                title="submenu",
                name="submenu",
                buttons=[
                    button := Back(title="back"),
                ],
            ),
        ],
        back_btn_title="back",
    )
    button._payload = "qwe"
    submenu._parent = menu
    with pytest.raises(ValueError):
        button._init(submenu, router, payload)


@pytest.mark.asyncio
async def test_build(callback_query, prefix):
    button = Back(title="back")
    button._payload = f"{prefix}##"
    button._visible = True
    result = await button._build(callback_query)
    assert result == InlineKeyboardButton(
        text="back",
        callback_data=button._payload,
    )


@pytest.mark.asyncio
async def test_build_not_visible(callback_query):
    button = Back(title="back")
    result = await button._build(callback_query)
    assert result is None
