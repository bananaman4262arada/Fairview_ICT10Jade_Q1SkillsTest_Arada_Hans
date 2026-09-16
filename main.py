from pyscript import document, display
        
def create_order(e):
       document.getElementById("output1").innerHTML = "" # clears previous result
       item1 = document.getElementById("item1")
       item2 = document.getElementById("item2")
       item3 = document.getElementById("item3")
       item4 = document.getElementById("item4")
       item5 = document.getElementById("item5")
       subtotal = (float(item1.value) * item1.checked) + (float(item2.value) * item2.checked) + (float(item3.value) * item3.checked) + (float(item4.value) * item4.checked) + (float(item5.value) * item5.checked)
       tax = subtotal * 0.12
       grandtotal = subtotal + tax
       display(f'SUBTOTAL               {subtotal}', target="output1", append=True)
       display(f'SALES TAX ON 7.34      {tax}', target="output1", append=True)
       display(f'TOTAL DUE              {grandtotal}', target="output1", append=True)order}', target="output4")
