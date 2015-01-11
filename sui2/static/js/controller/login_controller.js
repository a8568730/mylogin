angular.module('app1')
.controller('loginController', ['$scope', '$http', function($scope, $http){
	$scope.verified = false;
	
	$scope.login = function(){		
		//Goal - method POST
		$http({
			method: 'GET',
			url: '/' + $scope.un + '/' + $scope.pw + '/驗證使用者'
		})
		.success(function(data, status) {
				console.log(data);
				$scope.verified = data['verified'];
				console.log($scope.verified);
		});
	};
	
}]);