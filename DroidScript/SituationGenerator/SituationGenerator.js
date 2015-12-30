
//Called when application is started.
function OnStart()
{
	//Create a layout with objects vertically centered.
	lay = app.CreateLayout( "linear", "VCenter,FillXY" );	

	//Create a text label and add it to layout.
	txt = app.CreateText( "Situation Generator" );
	txt.SetTextSize( 16 );
	lay.AddChild( txt );
	
	btn = app.CreateButton( "Create Prompt" );
	btn.SetOnTouch( sentenceMasher );
	lay.AddChild( btn );
	
	Sentence1 = app.CreateText();
	Sentence1.SetTextSize( 12 );
	Sentence2 = app.CreateText();
	Sentence2.SetTextSize( 12 );
	
	//Add layout to app.	
	app.AddLayout( lay );
}

function sentenceMasher()
{
    lay.DestroyChild( Sentence1 );
    lay.DestroyChild( Sentence2 );
    
    var person = ["ともだち と ","おかあさん と ","かいちょう と "];
	var place = ["きみのうち に ","しごと に ","スーパー に "];
	var prompt = ["ききませんでした。","行きたい。","おくりもの を うけとります。"];
	var gen1 = Math.floor(Math.random()*3);
	var gen2 = Math.floor(Math.random()*3);
	var gen3 = Math.floor(Math.random()*3);
    
    Sentence1 = app.CreateText( "きみ は " + person[gen1] + place[gen2] + "います。" );
    Sentence2 = app.CreateText( prompt[gen3] );
    lay.AddChild( Sentence1 );
    lay.AddChild( Sentence2 );
    
}
