from typing import List

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from chef.controllers import RecipesController
from chef.models import engine
from chef.schemas import Recipe, CreateOrUpdateRecipe

router = APIRouter()
recipes = RecipesController()


# Store the current recipe id in memory
CURRENT_RECIPES_IDS = []


@router.get("")
async def get_recipes(category: int = None, favorite: bool = False) -> List[Recipe]:
    with Session(engine()) as session:
        if favorite:
            return await recipes.get_all_and_filter(session, favorite=favorite)
        if category:
            return await recipes.get_by_category(session, category)
        return await recipes.get_all(session)


@router.get("/{item_id}")
async def get_recipe(item_id: int) -> Recipe:
    with Session(engine()) as session:
        return await recipes.get_single(session, item_id)


@router.delete("/{item_id}")
async def delete_recipe(item_id: int) -> None:
    with Session(engine()) as session:
        await recipes.delete_single(session, item_id)


@router.post('', status_code=201)
async def create_recipe(create_data: CreateOrUpdateRecipe) -> Recipe:

    if any(not i.ingredient.name for i in create_data.ingredients):
        raise HTTPException(
            status_code=400,
            detail="Empty ingredient name not allowed."
        )

    with Session(engine()) as session:
        return await recipes.create(session, create_data)


@router.put('/{item_id}')
async def update_recipe(item_id: int, update_data: CreateOrUpdateRecipe) -> Recipe:

    if any(not i.ingredient.name for i in update_data.ingredients):
        raise HTTPException(
            status_code=400,
            detail="Empty ingredient name not allowed."
        )

    with Session(engine()) as session:
        return await recipes.update(session, item_id, update_data)
