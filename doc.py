from google.cloud import storage
import pandas as pd

# def chooseProduct(): 
#     choice = None
#     while choice not in ('a', 'b'):
#         inputValue = input("Si tu veux acheter écrit a, si tu veux vendre écrit b")
#         try:
#             # try and convert the string input to a number
#             choice = inputValue
#         except:
#             # tell the user off
#             print(f"{inputValue} n'est pas un choix valide")
    
#     return choice
        
    
def selBuy(choice):
    df = pd.read_csv(r'C:\Users\tbonn\OneDrive\Documents\1 - programming\StockManagement\mainData.csv', delimiter=',', encoding='ANSI')
    ref_prd = int(df['Ref_PRD'].max() +1)
    print(ref_prd)
    if choice == 'a':
        print("DIRECITON ACHAT")
        buyDate = input("date: ")
        Brand = input("Marque: ")
        Category = input("Category: ")
        Description = input ("Description: ")
        skuCode = input("SkuCode: ")
        taille = input("taille: ")
        buyingPrice = input("prix d'achat: ")
        forcastPrice = input("prix de revente prevue")

        df2 = df.append(pd.DataFrame({'Ref_PRD' : [ref_prd],
                            'buyDate' : [buyDate],
                            'saleDate' : [pd.NA],
                            'Brand' : [Brand],
                            'Category' : [Category],
                            'Description' : [Description],
                            'skuCode' :[skuCode],
                            'taille' : [taille],
                            'buyingPrice' : [buyingPrice],
                            'forcastPrice' : [forcastPrice],
                            'sellingPrice' : [pd.NA],
                            'salesPlace' : [pd.NA]}),ignore_index=True)

        print(df2.tail(10))

        
    
    
    else:
        print("DIRECITON VENTE")



def openBucket():
    project_id = "silver-nova-360910"
    bucket = 'vegastore'
    exportBucket = storage.Client(project=project_id).get_bucket(bucket)
    print(exportBucket)
    chunk = pd.read_csv(f'gs://vegastore/Stock/mainData.csv', sep=',', encoding = 'ANSI')
    chunk = chunk.applymap(lambda s: s.upper() if type(s) == str else s)
    print(chunk)


def lookupItem():
    lookupItem = str(input('what are you looking for')).upper()
    chunk = pd.read_csv(f'gs://vegastore/Stock/mainData.csv', sep=',', encoding = 'ANSI')
    chunk = chunk.applymap(lambda s: s.upper() if type(s) == str else s)
    chunk = chunk.loc[chunk["Description"].str.contains(lookupItem)]
    print(chunk)

















def main():
#    choice = chooseProduct()
#    selBuy(choice)
    openBucket()
    lookupItem()

if __name__ == "__main__":
    main()
 