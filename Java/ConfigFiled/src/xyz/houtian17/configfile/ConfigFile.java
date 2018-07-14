package xyz.houtian17.configfile;

import org.bukkit.plugin.java.JavaPlugin;

public class ConfigFile extends JavaPlugin {
    @Override
    public void onEnable() {
        getConfig().options().copyDefaults(true);
        saveConfig();
        getServer().getPluginManager().registerEvents(new playerJoin(this), this);
    }

    @Override
    public void onDisable() {
        saveConfig();
    }
}
