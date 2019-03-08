class ShoppingCart:
    # write your code here
    def __init__(self, total = 0, employee_discount=None, items=[]):
        self.total = total
        self.employee_discount = employee_discount
        self.items = items
    
    def add_item(self, name, price, quantity=1):
        item_dict = {'name':name, 'price':price}
        q = 1
        while q <= quantity: 
            self.items.append(item_dict)
            q+=1
            
        self.total = sum(item['price'] for item in self.items)

        print(self.total)
        
    def mean_item_price(self):
       return sum(item['price'] for item in self.items)/len(self.items)

    def median_item_price(self):
        #get list of prices in ascending order
        list_of_prices = []
        for item in self.items:
            list_of_prices.append(item['price'])
        
        list_of_prices_asc = sorted(list_of_prices)
        #print(list_of_prices_asc)
        
        #---get median---
        list_len = len(self.items)
        middle_index_odd = int(list_len/2-0.5)
        middle_index_even1 = int(list_len/2-1)
        middle_index_even2 = int(list_len/2+1)

        #If odd, get middle index
        if list_len % 2 !=0:
            median_price = list_of_prices_asc[middle_index_odd]
            return median_price
        else:
            median_price = (list_of_prices_asc[middle_index_even1] + list_of_prices_asc[middle_index_even2])/2
            return median_price
        
        #print(self.items)
        #print(self.items[middle_index_odd])


    def apply_discount(self):
        if self.employee_discount is not None:
            discount_multiplier = (1- (self.employee_discount*.01))
            self.total = self.total*discount_multiplier
            print(self.total)
        else:
            print('Sorry, there is no discount to apply to your cart :(')
   
   
    def void_last_item(self):
        print(self.items)
        print(self.items[-1])
        
        #del self.items[-1]