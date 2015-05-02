function Id(string) {
    return string.replace(' ', '-');
}


(function(){
    var app = angular.module('store', []);

    app.service('$categories', function(){
        this.selected = {a: null, b: null, c: null};
        this.changed = false;

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
    });

    app.directive('mainCategories', function(){
        return {
            restrict: 'E',
            templateUrl: '/static/mainCategories.html',
            controllerAs: 'categoryCtrl',
            controller: ['$http', '$categories', function($http, $categories){
                this.mainCategories = [];
                this.subCategories = [];

                this.parseCategoriesFromJSON = function(data){
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

                this.selectA = function (category){
                    $categories.selectA(category);
                };

                this.selectB = function (category){
                    $categories.selectB(category);
                };

                this.selectC = function (category){
                    $categories.selectC(category);
                };
                
                ctrl = this;
                $http.get('/api/categories').success(function(data){
                    ctrl.parseCategoriesFromJSON(data);
                });
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
