package main

import "testing"

func Test16(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("16 Error, got %d", r)
	}
}
