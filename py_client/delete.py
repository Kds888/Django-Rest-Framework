import requests

product_id = int(input("Enter the product_id you want to delete \n"))

delete_product = requests.delete(f"http://localhost:8000/products/genericdestroyview/{product_id}/")

# It will just delete the product 
print(delete_product.status_code,delete_product.status_code == 204) # 204 is the status code for delete 
# working and the product deleted success fully