angular.module('app1')
.controller('loginController', ['$scope', 'loginservice', function($scope, loginservice){
	
	$scope.arr = {};
	$scope.arr['verified'] = false;
	
	$scope.login = function(){ 
		loginservice.verify($scope.un, $scope.pw)
										.success(function(data){
												$scope.arr = data;
										}); 
	};
	
}]);