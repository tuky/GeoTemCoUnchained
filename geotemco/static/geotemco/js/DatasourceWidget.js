/**
 * widget to list all available datasources
 */
function DatasourceWidget(widgets,items,title,breaks){

	this.container = document.getElementById("datasourceDiv");

	this.header = document.createElement("div");
	this.header.setAttribute('class','dswHeader');
	this.header.innerHTML = title;
	this.container.appendChild(this.header);

	this.content = $("<div class='dswContent ui-state-default'/>").appendTo(this.container);

	var sortlist = $("<div id='sortlist'/>").appendTo(this.content);
	$(sortlist).css('max-height','200px');
	$(sortlist).css('overflow-x','none');
	$(sortlist).css('overflow-y','auto');
	for( var i in items ){
		var checkDiv = $("<div/>").appendTo(sortlist);
		if( breaks ){
			$(checkDiv).css('display','block');
		}
		var check = $("<input class='sourceCheckbox' type='checkbox'>"+items[i].title+"</input>").appendTo(checkDiv);
	}
	
	this.checkboxes = $('.sourceCheckbox');

	var widget = this;
	var buttonDiv = $("<div/>").appendTo(this.content);
	var setButton = $("<input type='submit' value='Set Data'/>").appendTo(buttonDiv);
	setButton.click(function(){
		var datasets = [];
		for( var i=0; i<widget.checkboxes.length; i++ ){
			if( $(widget.checkboxes[i]).attr('checked') ){
				if( typeof items[i].urls != "undefined" ){
					var data = [];
					for( var j=0; j<items[i].urls.length; j++ ){
						data = data.concat(GeoTemConfig.loadJson(GeoTemConfig.getJson(items[i].urls[j])));
					}
					datasets.push(new Dataset(data,items[i].title));
				}
				else if( items[i].url.indexOf('.kml') == -1 ){
					datasets.push(new Dataset(GeoTemConfig.loadJson(GeoTemConfig.getJson(items[i].url)),items[i].title));
				}
				else {
					datasets.push(new Dataset(GeoTemConfig.loadKml(GeoTemConfig.getKml(items[i].url)),items[i].title));
				}
			}
		}
		for( var i=0; i<widgets.length; i++ ){
			widgets[i].display(datasets);
		}
	});

}
