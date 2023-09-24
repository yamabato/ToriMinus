# ToriMinus

## 概要

　本プログラムは、数年前に作成されたTori-なる言語をC言語を用いて再実装したものである。

　Tori-は実装の簡便さを特に考慮して設計され、利便性等はほぼ顧慮されていない。本プログラムにおいては当時の仕様をそのまま再現している。

## 特徴

　Tori-は上述の通り、設計において実装の容易さを第一としている。そのため、複数の構文を設定することなく十分な機能を提供できるよう、多くの言語において文として扱うような条件分岐等を関数によって実現している。変数の代入も式として扱われるため、式文を除けば文に当たるのは関数定義と、pyfuncと呼ばれる関数を読み込むpyfunc文しかない。

　上の特徴のため、pyfuncなる機能を用いなければ変数代入や演算以外に実行可能な操作がない。従って、pyfuncと呼ばれるものがTori-において重要な役割を果たす。入出力や数値変換から、条件分岐や繰り返しなどのフロー制御まで幅広い機能がpyfuncによって提供される。その名の通り、pyfuncはPython実装ではPythonによって実装されていた。本実装ではCで実装されているが、名前は据え置きとした。

## 言語ドキュメント

　本言語のドキュメントは以下の通りです。
 
　## [ドキュメント](https://github.com/yamabato/ToriMinus/wiki/)

