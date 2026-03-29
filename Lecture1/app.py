from fastapi import FastAPI
from mockdata import products
from dtos import ProductDTO

app = FastAPI()

@app.get("/")
def home():
    return "FastAPI is Working"

# --- get all products --
@app.get("/products")
def get_product():
    return products

# ---- Get one Product ----
# ======================= path params ============
@app.get("/product/{product_id}")
def get_one_product(product_id:int):
    for one_poduct in products:
        if one_poduct.get("id") == product_id:
            return one_poduct
    
    return {
        "error": "Product not found"
    }

# -------------- Create new Product -------------
@app.post("/create_product")
def create_new_product(product_data:ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)
    return {
        "status":"Product Created Successfully",
        "data":products
    }

# ----------------- Update Product --------------
@app.put("/update_product/{product_id}")
def update_product(product_data:ProductDTO,product_id:int):
    for index, one_product in enumerate(products):
        if one_product.get("id") == product_id:
            products[index] = product_data
            return {
                "status":"Product updated successfully",
                "product":product_data
            }
    return {
        "error":"Product not found"
    }

# ----- Update baaki hai bhai ----------
@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
    for index, one_product in enumerate(products):
        if one_product.get("id") == product_id:
            deleted_product = products.pop(index)
            return {
                "status":"Product Delete Successfully",
                "deleted_product":deleted_product
            }
    return {
        "Error":"Product Not Found"
    }