                   
    
# Function to find RetailTxn & Lineitem tag. And to print the details
def RetailTxn_Tag(Txn_Tag):

    # Loop to go through all the children of Transaction tag
    for node in Txn_Tag:
        #print(node)
        if node.tag.split("}")[1] == "RetailStoreID":     #Prints StoreID
            print("StoreID","\t\t\t",node.text)
        if node.tag.split("}")[1] == "WorkstationID":     #Prints RegID
            print("RegisterID","\t\t\t",node.text)
        if node.tag.split("}")[1] == "BusinessDayDate":   #Prints TXN DATE
            print("Business Date","\t\t\t",node.text)
        if node.tag.split("}")[1] == "PosTransactionProperties":   
            # Loop to go through all the children nodes of PosTxnProperties tag
            for TxnProperty in node:
                if TxnProperty.tag.split("}")[1] == "PosTransactionPropertyCode" and TxnProperty.text == "TJX_TAX_EXEMPT_TYPE": #Prints Tax Exempt Type
                    name = node.find("{http://www.datavantagecorp.com/xstore/}PosTransactionPropertyValue")  
                    print("Tax Exempt Type","\t\t",name.text)
                if TxnProperty.tag.split("}")[1] == "PosTransactionPropertyCode" and TxnProperty.text == "TJX_STYLEPLUS_NUMBER": #Prints TJX Style+ Number
                    name = node.find("{http://www.datavantagecorp.com/xstore/}PosTransactionPropertyValue")  
                    print("TJX Style+ Number","\t\t",name.text)
                if TxnProperty.tag.split("}")[1] == "PosTransactionPropertyCode" and TxnProperty.text == "TJX_BLIND_RETURN_ID_TYPE": #Prints Unreceipted return id type
                    name = node.find("{http://www.datavantagecorp.com/xstore/}PosTransactionPropertyValue")  
                    print("Unreceipted Return ID type","\t",name.text)
                if TxnProperty.tag.split("}")[1] == "PosTransactionPropertyCode" and TxnProperty.text == "TJX_REWARDS_RETURN_ID_COUNTRY": #Prints Unreceipted return id Country
                    name = node.find("{http://www.datavantagecorp.com/xstore/}PosTransactionPropertyValue")  
                    print("Unreceipted Return ID County","\t",name.text)
                if TxnProperty.tag.split("}")[1] == "PosTransactionPropertyCode" and TxnProperty.text == "TJX_REWARDS_RETURN_ID_STATE": #Prints Unreceipted return id State
                    name = node.find("{http://www.datavantagecorp.com/xstore/}PosTransactionPropertyValue")  
                    print("Unreceipted Return ID State","\t",name.text)
                if TxnProperty.tag.split("}")[1] == "PosTransactionPropertyCode" and TxnProperty.text == "APR_ANALYZE_TRANSACTION_ID": #Prints Appris reference code
                    name = node.find("{http://www.datavantagecorp.com/xstore/}PosTransactionPropertyValue")  
                    print("Appriss Reference code","\t\t",name.text)
                if TxnProperty.tag.split("}")[1] == "PosTransactionPropertyCode" and TxnProperty.text == "TJX_BLIND_RETURN_STATUS": #Prints Unreceipted Return Status
                    name = node.find("{http://www.datavantagecorp.com/xstore/}PosTransactionPropertyValue")  
                    print("Unreceipted Return Status","\t",name.text)
                if TxnProperty.tag.split("}")[1] == "PosTransactionPropertyCode" and TxnProperty.text == "TJX_REPRINT_NUMBER": #Prints reprint number
                    name = node.find("{http://www.datavantagecorp.com/xstore/}PosTransactionPropertyValue")  
                    print("Number of Reprints","\t\t",name.text)
                if TxnProperty.tag.split("}")[1] == "PosTransactionPropertyCode" and TxnProperty.text == "TJX_LOAN_IN_FROM_REGISTER": #Prints Paid in register#
                    name = node.find("{http://www.datavantagecorp.com/xstore/}PosTransactionPropertyValue")  
                    print("Loan IN from Register#","\t\t",name.text)
                if TxnProperty.tag.split("}")[1] == "PosTransactionPropertyCode" and TxnProperty.text == "TJX_LOAN_OUT_TO_REGISTER": #Prints Paid Out register#
                    name = node.find("{http://www.datavantagecorp.com/xstore/}PosTransactionPropertyValue")  
                    print("Loan IN from Register#","\t\t",name.text)

        # Control Txns like store/wkstn open/close, No Sale
        if node.tag.split("}")[1] == "ControlTransaction":
            for ctxn in node:
                if ctxn.tag.split("}")[1] == "ReasonCode":
                    print("Reason Code","\t\t\t",ctxn.text)

        # Paid In/Out
        if node.tag.split("}")[1] == "TenderControlTransaction":
            for contxn in node:
                if contxn.tag.split("}")[1] == "PaidIn":
                    for pd in contxn:
                        if pd.tag.split("}")[1] == "Amount":
                            print("Paid In Amount","\t\t\t",pd.text)        #Prints Paid IN amount

                if contxn.tag.split("}")[1] == "PaidOut":
                    for pd in contxn:
                        if pd.tag.split("}")[1] == "Amount":
                            print("Paid Out Amount","\t\t\t",pd.text)           #Prints Paid Out amount
        

        # Cash Deposit
        if node.tag.split("}")[1] == "CashDepositDate":
            print("Cash Deposit Date","\t\t",node.text)           #Prints Cash Deposit Date

        if node.tag.split("}")[1] == "CashDepositAmount":
            print("Cash Deposit AMT","\t\t",node.text)            #Prints Cash Deposit Amount

        # Reprint txn
        if node.tag.split("}")[1] == "TransactionLink":
            print("__________________________________________________")
            for rtxn in node:
                if rtxn.tag.split("}")[1] == "RetailStoreID":
                    print("Original txn Store#","\t\t",rtxn.text)
                if rtxn.tag.split("}")[1] == "WorkstationID":
                    print("Original txn Reg#","\t\t",rtxn.text)
                if rtxn.tag.split("}")[1] == "SequenceNumber":
                    print("Original txn#","\t\t\t",rtxn.text)
                if rtxn.tag.split("}")[1] == "BusinessDayDate":
                    print("Original txn date","\t\t",rtxn.text)
        #gift receipt       
        if node.tag.split("}")[1] == "LineItem":
            print("__________________________________________________")
            for gtxn in node:
                if gtxn.tag.split("}")[1] == "LineItemProperty":
                    for lineProperty in gtxn:
                        if lineProperty.tag.split("}")[1] == "LineItemPropertyCode" and lineProperty.text == "GIFT_RECEIPT_ITEM_ID": #Prints Item ID of GIft Receipt
                            name = gtxn.find("{http://www.datavantagecorp.com/xstore/}LineItemPropertyValue")  
                            print("Gifted Item ID","\t\t\t",name.text)
                        if lineProperty.tag.split("}")[1] == "LineItemPropertyCode" and lineProperty.text == "TOTAL_GIFT_RECEIPTS": #Prints number of GIft Receipt
                            name = gtxn.find("{http://www.datavantagecorp.com/xstore/}LineItemPropertyValue")  
                            print("Number of Gift rececipts\t",name.text)
                        if lineProperty.tag.split("}")[1] == "LineItemPropertyCode" and lineProperty.text == "TJX_ASSOCIATE_DISCOUNT_AIN": #Prints Discount AIN
                            name = gtxn.find("{http://www.datavantagecorp.com/xstore/}LineItemPropertyValue")  
                            print("AIN Number","\t\t\t",name.text)
                if gtxn.tag.split("}")[1] == "Discount":
                    for dgrec in gtxn:
                        if dgrec.tag.split("}")[1] == "DiscountId" :                #Prints discount ID of GIft Receipt
                            nm = DiscName(dgrec.text)
                            print("Discount on gifted item","\t",nm)
                        if dgrec.tag.split("}")[1] == "PercentOff" :                #Prints discount % of GIft Receipt
                            print("Discount% on gifted item","\t",int(float(dgrec.text)*100))
                            
        if node.tag.split("}")[1] == "RetailTransaction": 
                    Retail_Tag = node
                    
                    # Loop to go through all the children nodes of RetailTxn tag
                    for node in Retail_Tag:
                        if node.tag.split("}")[1] == "LineItem":
                            
                            # Loop to go through all the children nodes of Lineitm tag 
                            for nd in node:
                                if nd.tag.split("}")[1] == "Sale" or nd.tag.split("}")[1] == "Return":
                                    print("__________________________________________________")
                                    print("***************Item Details***************")

                                    #Loop to print the attributes of Sale/Return tag
                                    for k,v in node.attrib.items():
                                        if k =="VoidFlag":
                                            u = TrFa(v)
                                        if k =="EntryMethod":
                                            print("Item Entry Method","\t\t",v) #Prints Item Entry Method
                                    LineItemSale_Tag(nd,u)
                                if nd.tag.split("}")[1] == "Tax":
                                    print("***************Tax Details***************")

                                    #Loop to print the attributes of Txn Tax tag
                                    for k,v in node.attrib.items():
                                        if k =="VoidFlag":
                                            u = TrFa(v)
                                    LineItemTax_Tag(nd,u)
                                if nd.tag.split("}")[1] == "Tender":
                                    print("***************Tender Details***************")
                                    
                                    #Loop to print the attributes of Txn Tender tag
                                    for k,v in node.attrib.items():
                                        if k == "VoidFlag":
                                            u = TrFa(v)
                                        if k == "EntryMethod":
                                            print("Card Tender Entry Method","\t",v)#Prints Card Tender enter method
                                    LineItemTender_Tag(nd,u)                               
                                        
                        if node.tag.split("}")[1] == "SubTotal":
                            print("Txn Subtotal","\t\t\t",node.text)         #Prints Txn SubTotal
                        if node.tag.split("}")[1] == "Total":
                            print("Txn Total","\t\t\t",node.text)            #Prints Txn Total
                        if node.tag.split("}")[1] == "RoundedTotal":
                            print("Txn Rounded Total","\t\t",node.text)      #Prints Txn Rounded Total
                        if node.tag.split("}")[1] == "Customer":
                            for cdetails in node:
                                if cdetails.tag.split("}")[1] == "Name":
                                    print("Customer Name","\t\t\t",cdetails.text) #Prints Customer Name
# Function to Print Sale/Return Lineitem tag details
def LineItemSale_Tag(Litm,u):
    for node in Litm:
        
        if node.tag.split("}")[1] == "DepartmentNumber":
            print("Department Number","\t\t",u+node.text)                     #Prints Item's DeptNo
        if node.tag.split("}")[1] == "Description":
            print("Department Description","\t\t",u+node.text)                #Prints Item's Dept Description
        if node.tag.split("}")[1] == "StyleNumber":
            print("Style Number","\t\t\t",u+node.text)                        #Prints Item's StyleNo
        if node.tag.split("}")[1] == "ScannedItemID":
            print("ItemID","\t\t\t\t",u+node.text)                            #Prints Item's ItemID
        if node.tag.split("}")[1] == "RegularSalesUnitPrice":
            print("Unit Price","\t\t\t",u+node.text)                          #Prints Item's Unit Price
        if node.tag.split("}")[1] == "ExtendedAmount":
            print("Extended Price","\t\t\t",u+node.text)                      #Prints Item's Actual Price
        if node.tag.split("}")[1] == "TaxIndicator":
            print("Tax Indicator","\t\t\t",u+node.text)
        if node.tag.split("}")[1] == "OriginalItemTaxGroupId":
            print("Original TaxGroup ID","\t\t",u+node.text)
        if node.tag.split("}")[1] == "RetailPriceModifier":
            for k,v in node.attrib.items():
                if k =="VoidFlag":
                    u = TrFa(v)
            #Loop to access Item's Discount children nodes
            for n1 in node:
                if n1.tag.split("}")[1] == "Amount":
                    print("Item Discount Amount","\t\t",u+n1.text)            #Prints Item's discount amount
                if n1.tag.split("}")[1] == "Percent":
                    print("Item Discount Percent","\t\t",u+str(int(float(n1.text)*100))+"%")#Prints Item's discount%
                if n1.tag.split("}")[1] == "PromotionID":                   
                    nm = DiscName(n1.text)
                    print("Item Discount Name","\t\t",u+nm)              #Prints Item's discount name
        if node.tag.split("}")[1] == "Tax":

            #Loop to access Item's Tax children nodes
            for n1 in node:
                if n1.tag.split("}")[1] == "Amount":
                    print("Item Tax Amount","\t\t",u+n1.text)                 #Prints Item's Tax amount
                if n1.tag.split("}")[1] == "Percent":
                    print("Item Tax Percent","\t\t",u+str(float(n1.text)*100)+"%")#Prints Item's Tax%
                if n1.tag.split("}")[1] == "TaxableAmount":
                    print("Item Taxable Amount","\t\t",u+n1.text)             #Prints Item's Taxable Amt
                if n1.tag.split("}")[1] == "TaxGroupId":
                    print("Item TaxGroup ID","\t\t",u+n1.text)             #Prints Item's Tax group id
                if n1.tag.split("}")[1] == "TaxOverride":
                    for taxov in n1:
                        if taxov.tag.split("}")[1] == "ReasonCode":
                            print("Tax Exempt Type\t\t\t",u+taxov.text)
    print("__________________________________________________")

# Function to print the Txn TAX details
def LineItemTax_Tag(tax,u):

    #Loop to access Txn Tax children nodes
    for n1 in tax:
        if n1.tag.split("}")[1] == "Amount":
            print("Txn Tax Amount","\t\t\t",u+n1.text)                        #Prints Txn Tax Amt
        if n1.tag.split("}")[1] == "Percent":
            print("Txn Tax Percent","\t\t",u+str(float(n1.text)*100)+"%")     #Prints Txn Tax%
        if n1.tag.split("}")[1] == "TaxableAmount":
            print("Txn Taxable Amount","\t\t",u+n1.text)
        if n1.tag.split("}")[1] == "TaxAuthority":
            print("Txn Tax type","\t\t\t",u+n1.text)                          #Prints Txn Tax Authority
    print("__________________________________________________")

# Function to print the Txn TENDER details
def LineItemTender_Tag(tndr,u):
    #print(tndr.attrib)
    for k,v in tndr.attrib.items():
        if k == "{http://www.datavantagecorp.com/xstore/}ChangeFlag":
            c = Change(v)
    #Loop to access Tender children nodes
    for n1 in tndr:
        if n1.tag.split("}")[1] == "TenderID":
            print("Tender Type","\t\t\t",c+u+n1.text)                           #Prints TenderID
        if n1.tag.split("}")[1] == "Amount":
            print("Tender Amount","\t\t\t",c+u+n1.text)                        #Prints Tender Amt 

        #For Card tenders
        if n1.tag.split("}")[1] == "Authorization":
            for node in n1:
                if node.tag.split("}")[1] == "AuthorizationCode":
                    print("Card Auth Code","\t\t\t",u+node.text)         #Prints Card Auth Code
                if node.tag.split("}")[1] == "ReferenceNumber":
                    print("Card Sequence#","\t\t",u+node.text)           #Prints Card Sequence#
        if n1.tag.split("}")[1] == "CreditDebit":
            for node in n1:
                if node.tag.split("}")[1] == "MaskedCardNumber":
                    print("Card#","\t\t\t",u+node.text)                     #Prints Card#
                if node.tag.split("}")[1] == "AuthorizationToken":
                    print("Auth Token","\t\t",u+node.text)                  #Prints Auth Token
                if node.tag.split("}")[1] == "ExpirationDate":
                    print("Expiration Date","\t\t",u+node.text)              #Prints Expiration Date
        #For SSV tender
        if n1.tag.split("}")[1] == "Voucher":
            for node in n1:
                if node.tag.split("}")[1] == "FaceValueAmount":
                    print("Face Value","\t\t\t",u+node.text)           #Prints SS Voucher Face Value Amt
                if node.tag.split("}")[1] == "TjxSsvsVchr":
                    print("","\t\t\t",u+node.text)                      #Prints SS Voucher number

         #For Foreign Currency           
        if n1.tag.split("}")[1] == "ForeignCurrency":
            for node in n1:
                if node.tag.split("}")[1] == "OriginalFaceAmount":
                    print("Amt in USD","\t\t\t",u+node.text)            #Prints USD amount
                if node.tag.split("}")[1] == "ExchangeRate":
                    print("Exchange Rate","\t\t\t",u+node.text)         #Prints Exchange rate
    print("__________________________________________________")

# Function to convert flags value to YES/NO     
def TrFa(result):
    if result == "false":
        return ""
    if result == "true":
        return "V "
# Function to convert change flags value to YES/NO     
def Change(result):
    if result == "false":
        return ""
    if result == "true":
        return "C "
    
def DiscName(discode):
    if discode[-2:] == "07":
        return "VIP"
    if discode[-2:] == "01":
        return "ASSOC 10%"
    if discode[-2:] == "02":
        return "ASSOC OTHER%"
    if discode[-2:] == "03":
        return "ASSOC 20%"
    if discode[-2:] == "60" and discode[-3:] == "060":
        return "MANUAL TXN% OFF"
    if discode[-2:] == "60" and discode[-3:] == "160":
        return "MANUAL ITEM% OFF"
    
    
import xml.etree.ElementTree as ET
tree= ET.parse(r"C:\Users\puneet.f.jain\Music\PosLog.xml")  #XML File Path
root = tree.getroot() #Finds the root node i.e. POSLog
cnt = 0
print(" ENTER THE TXN NUMBER TO SEE THE POSLOG.")
User_Input = input()#Input for txn id
# Child Parent Mapping for all the elements of XML
parent_map = dict((c, p) for p in tree.getiterator() for c in p)

#Loop to find the txn enter by user in xml file        
for txn in root.findall("./{http://www.nrf-arts.org/IXRetail/namespace/}Transaction/{http://www.nrf-arts.org/IXRetail/namespace/}SequenceNumber"):
    if txn.text == User_Input:
        cnt = cnt + 1
        print("***************Transaction Details***************")
        print("TransactionID","\t\t\t",txn.text)                        #Prints the TxnID
        for k,v in parent_map.items():
            if k == txn:
                Txn_Tag = v
                for k,v in Txn_Tag.attrib.items():
                    if k =="CancelFlag":
                        print("Cancel","\t\t\t\t",v)                    #Prints the Cancel Flag Value
                    if k =="OfflineFlag":
                        print("Offline","\t\t\t",v)                     #Prints the Offline Flag Value
                    if k =="{http://www.datavantagecorp.com/xstore/}TransactionType":
                        print("Txn Type","\t\t\t",v)                    
                RetailTxn_Tag(Txn_Tag)
if cnt ==0:
    print("TXN NOT FOUND! PLEASE ENTER CORRECT TXN# OR USE CORRECT POSLOG FILE.")
