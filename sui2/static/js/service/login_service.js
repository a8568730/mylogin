angular.module('app1')
.service('loginservice', ['$http', function($http) {
	
		this.verify = function(un, pw){
				//Goal - method POST
				return 	$http({
					method: 'GET',
					url: '/' + un + '/' + pw + '/驗證使用者'
				});
		};
	
}]);