/*jslint indent: 2*/
/*global angular, jQuery*/

var mxApp = angular.module('mxApp', []);

mxApp.controller('MxCtrl', function ($scope) {
  'use strict';
  $scope.check = function () {
    $scope.showResult = false;
    $scope.showLoad = true;
    jQuery.ajax({
      url: '/api/',
      data: {domain: $scope.domain},
      success: function (result) {
        $scope.result = result;
        $scope.showLoad = false;
        $scope.showResult = true;
        $scope.$digest();
      },
      error: function (result) {
        $scope.result = result.responseJSON;
        $scope.showLoad = false;
        $scope.showResult = true;
        $scope.$digest();
      }
    });
  };

  $scope.domain = '';
  $scope.showLoad = false;
  $scope.showResult = false;
});
