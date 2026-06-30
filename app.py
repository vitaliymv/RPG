import streamlit as st
import json
from hero import Hero

st.set_page_config(page_title="RPG", layout="wide")
st.title("RPG Hero")

if "hero" not in st.session_state:
    st.session_state.hero = None

if st.session_state.hero is None:
    st.subheader("Create your own hero")
    name = st.text_input("Hero name")
    hero_class = st.selectbox("Class", ["Warrior", "Mage", "Archer"])
    if st.button("Create"):
        if name:
            st.session_state.hero = Hero(name, hero_class)
            st.rerun()
else:
    hero = st.session_state.hero
    col1, col2 = st.columns([1, 2])

    with col2:
        st.subheader("Actions")
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("Fight"):
                monster, dmg, gold, exp = hero.fight()
                st.success(f"You won the {monster}")
                st.warning(f"You lost {dmg} hp")
                st.success(f"You got {gold} gold")
                st.info(f"You got {exp} exp")
        with c2:
            if st.button("Train"):
                if hero.train():
                    st.success("Strength and defense is increased")
                else:
                    st.error("Not enough gold")
        with c3:
            if st.button("Heal"):
                if hero.heal():
                    st.success("Your hp was restored")
                else:
                    st.error("Not enough a gold")

        st.divider()
        shop = {
            "Wood sword (+1 strength) 50gold": {
                "price": 50,
                "strength": 1
            },
            "Iron shield (+1 defense) 50gold": {
                "price": 50,
                "defense": 1
            }
        }
        item = st.selectbox("Choose item", list(shop.keys()))
        if st.button("Buy item"):
            product = shop[item]
            if hero.gold >= product["price"]:
                hero.add_item(item, product)
                hero.gold -= product["price"]
                st.success(f"You bought: {item}")
            else:
                st.error("Not enough gold")
        st.divider()

        st.subheader("Inventory")
        if len(hero.inventory) == 0:
            st.write("Empty")
        else:
            for item in hero.inventory:
                st.write("*", item)
        st.divider()
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Save game"):
                with open("save.json", "w", encoding="utf-8") as f:
                    json.dump(hero.to_dict(), f, ensure_ascii=False, indent=4)
                st.success("Game saved")
        with c2:
            if st.button("Load game"):
                try:
                    with open("save.json", "r", encoding="utf-8") as f:
                        data = json.load(f)
                        st.session_state.hero = Hero.from_dict(Hero, data)
                        st.success("Game loaded")
                        st.rerun()
                except:
                    st.error("File not found")
    with col1:
        st.subheader("Hero")
        st.write(f"Name: {hero.name}")
        st.write(f"Hero class: {hero.hero_class}")
        st.write(f"HP: {hero.hp} / {hero.max_hp}")
        st.progress(hero.hp / hero.max_hp)
        st.write(f"Level: {hero.level}")
        st.write(f"Experience: {hero.exp}")
        st.write(f"Gold: {hero.gold}")
        st.write(f"Strength: {hero.strength}")
        st.write(f"Defense: {hero.defense}")
