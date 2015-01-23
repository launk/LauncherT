//    LauncherT
//    Copyright © 2015  RunasSudo
//
//    This program is free software: you can redistribute it and/or modify
//    it under the terms of the GNU General Public License as published by
//    the Free Software Foundation, either version 3 of the License, or
//    (at your option) any later version.
//
//    This program is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//    GNU General Public License for more details.
//
//    You should have received a copy of the GNU General Public License
//    along with this program.  If not, see <http://www.gnu.org/licenses/>.

package io.github.runassudo.launchert;

import java.util.ArrayList;

import android.appwidget.AppWidgetHostView;
import android.appwidget.AppWidgetManager;
import android.graphics.Rect;
import android.os.Build;
import android.os.Bundle;

public interface AppsCustomizeView extends LauncherTransitionable {
	/**
     * The different content types that this paged view can show.
     */
    public enum ContentType {
        Applications,
        Widgets
    }
    
    public void loadCurrentPage(); // = loadCurrentPage(false)
    public void loadCurrentPage(boolean immediateAndOnly);
    
    public void setWidgetsPageIndicatorPadding(int pageIndicatorHeight);
    
    public void clearAllWidgetPages();
    public void setContentType(ContentType type);
    public ContentType getContentType();
    public void reset();
    public void setPageBackgroundsVisible(boolean visible);
    public void setup(Launcher launcher, DragController dragController);
    public void setBulkBind(boolean bulkBind);
    public void surrender();
    public void restorePageForIndex(int index);
    public int getSaveInstanceStateIndex();
    public void setApps(ArrayList<AppInfo> list);
    public void addApps(ArrayList<AppInfo> list);
    public void onPackagesUpdated(ArrayList<Object> widgetsAndShortcuts);
    public void updateApps(ArrayList<AppInfo> list);
    public void removeApps(ArrayList<AppInfo> appInfos);
    public void dumpState();
}

class AppsCustomizeViewDefaults {
	private static Rect sTmpRect = new Rect();
	
	static Bundle getDefaultOptionsForWidget(Launcher launcher, PendingAddWidgetInfo info) {
        Bundle options = null;
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.JELLY_BEAN_MR1) {
            AppWidgetResizeFrame.getWidgetSizeRanges(launcher, info.spanX, info.spanY, sTmpRect);
            Rect padding = AppWidgetHostView.getDefaultPaddingForWidget(launcher,
                    info.componentName, null);

            float density = launcher.getResources().getDisplayMetrics().density;
            int xPaddingDips = (int) ((padding.left + padding.right) / density);
            int yPaddingDips = (int) ((padding.top + padding.bottom) / density);

            options = new Bundle();
            options.putInt(AppWidgetManager.OPTION_APPWIDGET_MIN_WIDTH,
                    sTmpRect.left - xPaddingDips);
            options.putInt(AppWidgetManager.OPTION_APPWIDGET_MIN_HEIGHT,
                    sTmpRect.top - yPaddingDips);
            options.putInt(AppWidgetManager.OPTION_APPWIDGET_MAX_WIDTH,
                    sTmpRect.right - xPaddingDips);
            options.putInt(AppWidgetManager.OPTION_APPWIDGET_MAX_HEIGHT,
                    sTmpRect.bottom - yPaddingDips);
        }
        return options;
    }
}
