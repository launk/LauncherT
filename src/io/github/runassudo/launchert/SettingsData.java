// LauncherT
// Copyright © 2015 RunasSudo (LauncherT)
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program. If not, see <http://www.gnu.org/licenses/>.

package io.github.runassudo.launchert;

import android.content.Context;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;

public class SettingsData {
	protected SettingsData() {}

	public static String desktopGridMode;
	public static float desktopGridCustomWidth, desktopGridCustomHeight;
	public static int desktopDefaultScreen;
	public static boolean desktopShowSearchbar;

	public static void loadSettings(Context context) {
		SharedPreferences sharedPref =
				PreferenceManager.getDefaultSharedPreferences(context);

		desktopGridMode = sharedPref.getString("desktop_grid_mode", "default");
		desktopGridCustomWidth =
				Float.parseFloat(sharedPref.getString(
						"desktop_grid_custom_width", "5"));
		desktopGridCustomHeight =
				Float.parseFloat(sharedPref.getString(
						"desktop_grid_custom_height", "5"));
		desktopShowSearchbar =
				sharedPref.getBoolean("desktop_show_searchbar", true);
	}
}
