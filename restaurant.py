import json

def get_rating(reviews):
   rating = 5
   if reviews:
      rating = sum(reviews) // len(reviews)
   return "⭐" * rating


   
with open('menu.json', 'r') as f:
   data = json.load(f)

items = data.get('items', [])

while True:
    print("-"*50)
    print("************  PYTHON RESTAURANT  ***************")
    print("-"*50)
    print('1. Show Menu \n2. Order Items  \n3. Add Items \n4. Add Rating \n5. Exit')
    print("-"*50)

    choice= 

    
    if choice == 1:
       print("-"*50)
       print('ID\tName\t\tPrice\tRating')
       print("-"*50)
       for item in items:
          print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}\t{get_rating(item.get("reviews", []))}')

       print("-"*50)
       print('show menu')

    
    elif choice == 2:
       ordered_items = {}
       order_items = list(map(int, input("Enter the item ID's that you want to try: ").split(',')))
       print("-"*50)
       print('ID\tName\t\tPrice')
       print("-"*50)
       total_bill=0
       for order_item in order_items:
            for item in items:
               if item['id'] == order_item:
                  

                  
       print("-*50")
       print(f'\t Total Amount: {total_bill}')
       print("-"*50)
       
    
    elif choice == 3:
      name = input("enter item name: ")
      item_price = int(input("enter the price: "))
      items.append({
         'id' : len(items) + 1, 
         'name' : name,
         'price' : item_price,
         'reviews' : []
      })
      data['items'] = items
      with open('menu.json', 'w') as f:
         json.dump(data, f)
      print('Item successfully added to the menu.')

    
    elif choice == 4:
      item_id = int(input('Enter the item id: '))
      rating=int(input('Give your rating 1-5: '))
      for i, item in enumerate(items):
         if item['id'] == item_id:
            items[i]['reviews'].append(rating)
            break
      print('Thank You. Your rating is recorded.')


   
    else:
      data['items'] = items
      with open('menu.json', 'w') as f:
         json.dump(data, f)
      print('Thank you')
      break