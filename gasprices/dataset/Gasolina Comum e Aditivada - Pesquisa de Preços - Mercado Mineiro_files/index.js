$(document).ready(function() {
    $("#btn-todas").hover(function() {
        $(this).addClass("hovered");
        $("#ulpesquisas").show().hover(null, function() {
            $(this).hide();
            $("#btn-todas").removeClass("hovered");
        });
    }, function() {

    })
});

function MM_showHideLayers() { //v9.0
  var i,p,v,obj,args=MM_showHideLayers.arguments;
  for (i=0; i<(args.length-2); i+=3) 
  with (document) if (getElementById && ((obj=getElementById(args[i]))!=null)) { v=args[i+2];
    if (obj.style) { obj=obj.style; v=(v=='show')?'visible':(v=='hide')?'hidden':v; }
    obj.visibility=v; }
}