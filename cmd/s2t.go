/*
Copyright © 2020 syfun <sunyu418@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
*/
package cmd

import (
	"fmt"
	"github.com/spf13/cobra"
	"os"
	"strconv"
	"time"
)

// s2tCmd represents the s2t command
var s2tCmd = &cobra.Command{
	Use:   "s2t",
	Short: "Timestamp to Time.",
	Args: cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		c := NewConfig(cmd)
		ts, err := strconv.ParseInt(args[0], 10, 64)
		checkErr(err)
		level, err := cmd.Flags().GetInt("level")
		checkErr(err)

		var t time.Time
		switch level {
		case 0:
			t = time.Unix(ts, 0)
		case 1:
			t = time.Unix(ts / 1000, 1000000 * (ts % 1000))
		case 2:
			t = time.Unix(ts / 1000000, 1000 * (ts % 1000000))
		case 3:
			t = time.Unix(ts / 1000000000,  ts % 1000000000)
		default:
			fmt.Println("Invalid timestamp level")
			os.Exit(1)
		}
		c.PrintTime(t)
	},
}

func init() {
	timeCmd.AddCommand(s2tCmd)

	// Here you will define your flags and configuration settings.

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// s2tCmd.PersistentFlags().String("foo", "", "A help for foo")

	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	// s2tCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
	s2tCmd.Flags().IntP("level", "e", 0,
		"Timestamp level.\n0: second, 1: millisecond\n2: microsecond, 3: nanosecond")
}
