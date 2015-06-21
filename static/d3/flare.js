
var allNodes = [];

var ChessNode = function(nameParam, parent){
	"use strict";
	this.name = nameParam;
	if (parent){
		parent.children.push(this);
	}
	allNodes.push(this);
};
ChessNode.prototype.addChild = function(child){
	"use strict";
	if (!child.name){
		 return;
	}
	if (!this.children){
		this.children = [];
	}
	this.children.push(child);
};
ChessNode.prototype.getChildrenByName = function(queryName, collection){
	if (!this.children || this.children.length === 0) {
		return collection;
	}
	if (!collection){
		collection = [];
	}
	for (var i =0, l = this.children.length; i < l; i++){
		if (this.children[i].name === queryName){
			retVal.push(queryName);
		}
		this.children[i].getChildrenByName(queryName, collection);
	}
	return collection;
};
ChessNode.prototype.getFirstChildByName = function(queryName){
	if (!this.children || this.children.length === 0) {
		return null;
	}
	for (var i =0, l = this.children.length; i < l; i++){
		if (this.children[i].name === queryName){
			return this.children[i];
		}
		else{
			var child =	this.children[i].getFirstChildByName(queryName);
			if (child) return child;
		}
	}
	return null;
	
}



var root = new ChessNode("Chess Lessons");
root.addChild(new ChessNode("Openings"));
root.addChild(new ChessNode("Mid Game"));
root.addChild(new ChessNode("End Game"));

var op = root.getFirstChildByName("Openings");
var categories = ["A", "B", "C", "D", "E"];
for (var i = 0, l = categories.length; i < l ; i++)
	op.addChild(new ChessNode(categories[i]));
	
var catA = root.getFirstChildByName("A");
catA.addChild(new ChessNode("Ruy Lopez"));
catA.addChild(new ChessNode("Komodo vs. Dragon"));

var catB = root.getFirstChildByName("B");
catB.addChild(new ChessNode("Random Thing"));
catB.addChild(new ChessNode("Other Thing"));