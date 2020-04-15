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
	"time"

	"github.com/spf13/cobra"
)

// timeCmd represents the time command
var timeCmd = &cobra.Command{
	Use:   "t",
	Short: "Time tool",
	Long:  `Show time and convert between time and timestamp`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("time called")
	},
}

func init() {
	rootCmd.AddCommand(timeCmd)

	// Here you will define your flags and configuration settings.

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// timeCmd.PersistentFlags().String("foo", "", "A help for foo")
	timeCmd.PersistentFlags().String("tz", "UTC", "Time zone")
	timeCmd.PersistentFlags().String("l", time.RFC3339, "Time layout")

	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	// timeCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}

// Config represents time config.
type Config struct {
	// Location shows time zone.
	Location *time.Location

	// Format shows time format.
	Layout string
}

func NewConfig(cmd *cobra.Command) *Config {
	tz, err := cmd.Flags().GetString("tz")
	checkErr(err)

	location, err := time.LoadLocation(tz)
	checkErr(err)

	layout, err := cmd.Flags().GetString("l")
	checkErr(err)
	return &Config{Location: location, Layout: layout}
}

func (c *Config) PrintTime(t time.Time) {
	fmt.Println(c)
	fmt.Printf("%v: %v\n", c.Location, t.In(c.Location).Format(c.Layout))
	fmt.Printf("Local: %v\n\n", t.Local().Format(c.Layout))

	fmt.Println("Second timestamp:    ", t.Unix())
	fmt.Println("Nanosecond timestamp:", t.UnixNano())
}
