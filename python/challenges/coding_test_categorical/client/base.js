function Id(string) {
    return string.replace(' ', '-');
}


(function(){
    var app = angular.module('store', []);

    app.service('$categories', ['$http', function($http){
        this.selected = {a: null, b: null, c: null};
        this.changed = false;
	this.categories = [];

        this.selectA = function(category){
            if (this.selected['a'] != category){
                this.selected['a'] = category;
                this.selected['b'] = null;
                this.selected['c'] = null;
                this.changed = true;
            }
        }

        this.selectB = function(category){
            if (this.selected['b'] != category){
                this.selected['b'] = category;
                this.selected['c'] = null;
                this.changed = true;
            }
        }

        this.selectC = function(category){
            if (this.selected['c'] != category){
                this.selected['c'] = category;
                this.changed = true;
            }
        }

        this.validCategoriesSelected = function(){
            for (attr in this.selected) {
                if (this.selected[attr] == null){
                    return false;
                }
            }

            return true;
        };

        this.wereChanged = function(){
            var ret = this.changed;
            this.changed = false;
            return ret;
        };

	this.parseFromJSON = function(data){
            this.categories = [];
            for (categoryName in data){
                var subCategories = [];
                for (subCategoryName in data[categoryName]) {
                    var subSubCategories = [];
                    for (var name in data[categoryName][subCategoryName]) {
                        subSubCategories.push(name);
                    };

                    var subCategory = {
                        name: subCategoryName,
                        id: Id(categoryName + "-" + subCategoryName),
                        subSubCategories: subSubCategories,
                    };
                    subCategories.push(subCategory);
                };
                var category = {
                    name: categoryName,
                    id: Id(categoryName), subCategories: subCategories
                };
                this.categories.push(category);
            }
	};

        service = this;
        $http.get('/api/categories').success(function(data){
            service.parseFromJSON(data);
        });

	this.get = function(){
	    return this.categories;
	};
    }]);

    app.directive('mainCategories', function(){
        return {
            restrict: 'E',
            templateUrl: '/static/mainCategories.html',
            controllerAs: 'categoryCtrl',
            controller: ['$http', '$categories', function($http, $categories){
		this.categories = $categories.categories;

		this.get = function(){
		    return $categories.get();
		};

                this.selectA = function (category){
                    $categories.selectA(category);
                };

                this.selectB = function (category){
                    $categories.selectB(category);
                };

                this.selectC = function (category){
                    $categories.selectC(category);
                };
            }],
        };
    });

    app.directive('itemList', function(){
    return {
        restrict: 'E',
        templateUrl: '/static/itemList.html',
        controllerAs: 'itemList',
        controller: ['$http', '$categories', function($http, $categories){
            this.all_items = [];
            this.test = 'test';

            this.getAll = function(){
                if (($categories.wereChanged()) && ($categories.validCategoriesSelected())) {
                    url = '/api/list/' + $categories.selected['a'] + '/' + $categories.selected['b'] + '/' + $categories.selected['c'];
                    ctrl = this;
                    $http.get(url).success(function(data){
                        ctrl.all_items = data;
                    });
                };

                return this.all_items;
            };
        }],
    };
    });
})();
