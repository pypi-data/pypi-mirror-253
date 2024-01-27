package main

import (
	"C"
	"encoding/json"
	"errors"
	"fmt"
	rpmdb "github.com/knqyf263/go-rpmdb/pkg"
	"os"
	"path/filepath"
)

//export getrpmdbInfo
func getrpmdbInfo(fileNameIn *C.char) *C.char {
	return C.CString(getrpmdbInfodInfoInternal(C.GoString(fileNameIn)))
}

func main() {
	//getgobuildinfo(C.CString("foo/bar"))
	//getgobuildinfo(C.CString("/usr/bin/du"))
	//getgobuildinfo(C.CString("/Users/mike/go/pygobuildinfo/spire/support/oidc-discovery-provider/oidc-discovery-provider.elf"))
	//getgobuildinfo(C.CString("/Users/mike/go/pygobuildinfo/spire/support/oidc-discovery-provider/oidc-discovery-provider.exe"))
	//getgobuildinfo(C.CString("/Users/mike/go/pygobuildinfo/spire/support/oidc-discovery-provider/oidc-discovery-provider"))
}

func getrpmdbInfodInfoInternal(fileName string) string {
	returnValue := "{ \"error\" : \"Unknown\" }"
	db, err := rpmdb.Open(fileName)
	if err != nil {
		if pathErr := (*os.PathError)(nil); errors.As(err, &pathErr) && filepath.Clean(pathErr.Path) == filepath.Clean(fileName) {
			returnValue = fmt.Sprintf("{ \"error\": \"path error:%v\" }", fileName)
		} else {
			returnValue = fmt.Sprintf("{ \"error\": \"%s: %v\"}", fileName, err)
		}
	} else {
		pkgList, err := db.ListPackages()
		if err != nil {
			returnValue = fmt.Sprintf("{ \"error\": \"%s: %v\"}", fileName, err)
		} else {
			mySlice := []rpmdb.PackageInfo{}
			for _, pkg := range pkgList {
				mySlice = append(
					mySlice,
					*pkg)
			}
			data, _ := json.Marshal(mySlice)
			returnValue = string(data)
		}
	}
	// fmt.Printf("%s\n", returnValue)
	return returnValue
}
