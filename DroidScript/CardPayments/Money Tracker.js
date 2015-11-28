
//Called when application is started.
function OnStart()
{
    //Create a layout with objects vertically centered.
    layVert = app.CreateLayout( "linear", "VCenter,FillXY" );    

    //Create a text label and add it to layout.
    title = app.CreateText( "Credit Card" );
    title.SetTextSize( 32 );
    layVert.AddChild( title );
        
    layHorz1 = app.CreateLayout( "linear", "horizontal,FillX" );
    layVert.AddChild( layHorz1 );
    
    chargeTotal = app.LoadNumber("charges",0)
    curCharges = app.CreateText("$" + chargeTotal);
    curCharges.SetSize(0.4,0.1);
    curCharges.SetTextSize( 24 );
    layHorz1.AddChild(curCharges);
    
    paymentsTotal = app.LoadNumber("payments",0)
    curPayments = app.CreateText("$" + paymentsTotal);
    curPayments.SetSize(0.4,0.1);
    curPayments.SetTextSize( 24 );
    layHorz1.AddChild(curPayments);
    
    layHorz2 = app.CreateLayout( "linear", "horizontal,FillX" );
    layVert.AddChild(layHorz2);
    
    changeCharges = app.CreateTextEdit( "0.00", 0.3, 0.1)
    layHorz2.AddChild(changeCharges);
    
    btnCharge = app.CreateButton("Add Chrg", 0.1, 0.1);
    btnCharge.SetOnTouch(AddCharges);
    layHorz2.AddChild(btnCharge);
    
    changePayments = app.CreateTextEdit( "0.00", 0.3, 0.1)
    layHorz2.AddChild(changePayments);
    
    btnPay = app.CreateButton("Add Pay", 0.1, 0.1);
    btnPay.SetOnTouch(AddPayments);
    layHorz2.AddChild(btnPay);

    btnRst = app.CreateButton("Reset For Month", 0.8,0.1);
    btnRst.SetOnTouch(ResetValues);
    layVert.AddChild(btnRst);
    
    btnUndo = app.CreateButton("Undo", 0.8,0.1);
    btnUndo.SetOnTouch(ConfirmUndo);
    layVert.AddChild(btnUndo);
    
    //num = app.LoadNumber( "MyNumber", 42 );
    //app.ShowPopup( num );
    //app.SaveNumber( "MyNumber", num+1 );
    
    //Add layout to app.    
    app.AddLayout( layVert );
}

function AddCharges()
{
    //Add value to Charges
    chargeBackup = chargeTotal;
    enteredChargeValue = changeCharges.GetText();
    chargeTotal = chargeTotal + parseFloat(enteredChargeValue, 10);
    app.SaveNumber("charges", chargeTotal);
    app.RemoveLayout(layVert);
    OnStart();
    app.ShowPopup("Charge Added: $" + chargeTotal);
}

function AddPayments()
{
    //Add value to Payments
    paymentsBackup = paymentsTotal;
    enteredPaymentValue = changePayments.GetText();
    paymentsTotal = paymentsTotal + parseFloat(enteredPaymentValue, 10);
    app.SaveNumber("payments", paymentsTotal);
    app.RemoveLayout(layVert);
    OnStart();
    app.ShowPopup("Payment Added");
}

function ResetValues()
{
    //Confirm dialog, then reset values to 0
    booleanValue = null
    dlg = app.CreateListDialog("Confirm","Yes,No");
    dlg.SetOnTouch(ConfirmReset);
}

function ConfirmReset(item)
{
    booleanValue = item
    if (booleanValue =="Yes") {
        app.SaveNumber("charges",0);
        app.SaveNumber("payments",0);
        app.RemoveLayout(layVert);
        OnStart();
        app.ShowPopup("Records Reset");}
    else {
        app.ShowPopup("Records Not Reset");}
}

function ConfirmUndo()
{
    booleanValue = null
    dlgU = app.CreateListDialog("Confirm","Yes,No");
    dlgU.SetOnTouch(IFdUp);
}

function IFdUp(item)
{
    booleanValue = item
    if (booleanValue == "Yes") {
        try {
            app.SaveNumber("charges",chargeBackup)
            delete chargeBackup
            app.RemoveLayout(layVert);
            OnStart();
        }
        catch (e) {
        }
        try {
            app.SaveNumber("payments",paymentsBackup)
            delete paymentsBackup
            app.RemoveLayout(layVert);
            OnStart();
        }
        catch (e) {
        }
        app.ShowPopup("Undo complete");
    } else {
        app.ShowPopup("Not Undone");
    }
}
