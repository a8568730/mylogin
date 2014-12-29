/* 解決 Django 和 AngularJS共用{{}}的混淆問題 */
angular.module('app1')
.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});